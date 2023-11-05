from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flask_login import login_user, current_user, logout_user, login_required
from app.extensions import db
# from app import db
from app.models import User, Video, Like, Share, Comment
from app.forms import RegistrationForm, LoginForm, VideoUploadForm
from flask import jsonify

bp=Blueprint('sample', __name__)

@bp.route('/')
def home():
    videos = Video.query.all()

    like_counts = {}  # Dictionary to store like counts for each video

    for video in videos:
        # Count the likes for each video
        like_count = Like.query.filter_by(video_id=video.id).count()
        like_counts[video.id] = like_count

    return render_template('home.html', videos=videos, like_counts=like_counts)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('sample.home'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('sample.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('sample.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('sample.home'))
        else:
            print('Login unsuccessful. Please check your email and password.')
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', title='Log In', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('sample.home'))

@bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = VideoUploadForm()
    if form.validate_on_submit():
        video = Video(title=form.title.data, description=form.description.data, user=current_user)
        video_path = form.save_video()
        video.video = form.title.data+'.mp4'  
        db.session.add(video)
        db.session.commit()
        flash('Video uploaded successfully!', 'success')
        return redirect(url_for('sample.home'))
    return render_template('upload.html', title='Upload Video', form=form)

@bp.route('/video/<int:video_id>', methods=['GET', 'POST'])
def video(video_id):
    video = Video.query.get(video_id)
    if not video:
        abort(404)

    like_count = Like.query.filter_by(video_id=video_id).count()

    return render_template('video.html', video=video, like_count=like_count)

@bp.route('/like/<int:video_id>', methods=['POST'])
def like(video_id):
    print("inside like method")
    video = Video.query.get(video_id)
    
    if video:
        print(video)
        like = Like(user_id=current_user.id, video_id=video.id)
        db.session.add(like)
        db.session.commit()
        print("returning Liked")
        like_count = str(Like.query.filter_by(video_id=video_id).count())
        return like_count
    return "Error"

@bp.route('/comment/<int:video_id>', methods=['POST'])
def comment(video_id):
    text = request.form.get('text')
    video = Video.query.get(video_id)
    if video:
        new_comment = Comment(user_id=current_user.id, video_id=video.id, text=text)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({"text": new_comment.text})
    return "Error"
