
# REEL - APP

A simple web application similar to Reels, built with Flask.
## Features

- User authentication (login/logout/register)
- Video uploading
- Video streaming
- Liking and commenting on videos

# Setting Up a Python Flask Project

In this guide, we will walk you through the steps to set up a Python Flask project, including creating a virtual environment, installing project dependencies from a `requirements.txt` file, and running the Flask app.

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- Python 3.x: Download Python

## Step 1: Clone Your Flask Project

If you haven't already, clone your Flask project from a version control repository or copy the project files to a directory of your choice.

## Step 2: Delete Old Virtual Environment (Optional)

If you have an existing virtual environment and want to start fresh, you can delete it. Skip this step if you prefer to use your existing virtual environment.

### On Windows:

```bash
rmdir /s /q venv
```

### On macOS and Linux:

```bash
rm -r venv
```
or 

Delete the venv manually 

 
## Step 3: Create a New Virtual Environment

Navigate to your project directory using your terminal or command prompt and create a new virtual environment. Replace `venv` with your preferred virtual environment name:

```bash
python -m venv venv
```

## Step 4: Activate the Virtual Environment

Activate the newly created virtual environment:

### On Windows:

```bash
venv\Scripts\activate
```

### On macOS and Linux:

```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating that the virtual environment is active.

## Step 5: Install Project Dependencies

Install the project's dependencies from the `requirements.txt` file. Ensure you are in the project directory where the `requirements.txt` file is located:

```bash
pip install -r requirements.txt
```

## Step 6: Set the Flask App

Set the `FLASK_APP` environment variable to the name of your Flask application file (e.g., `run.py` or your project's main file):

### On Windows:

```bash
set FLASK_APP=run.py
```

### On macOS and Linux:

```bash
export FLASK_APP=run.py
```

## Step 7: Run the Flask App

You are now ready to run your Flask app. Start the Flask development server with the following command:

```bash
flask run
```

Your Flask app should now be running, and you can access it by opening a web browser and navigating to http://localhost:5000 by default.

## Step 8: Deactivate the Virtual Environment

To deactivate the virtual environment and return to the global Python environment, simply run:

### On Windows:

```bash
venv\Scripts\deactivate
```

### On macOS and Linux:

```bash
deactivate
```


