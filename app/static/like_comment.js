
$(document).ready(function() {
    
    $(".like-button").click(function() {
        var videoId = $(this).data("video");
        $.post("/like/" + videoId, function(data) {
            console.log(data)
            if (data >=0) {
                $(".like-count").text((data) + " likes");
            } else {
                console.log("Error while liking the video.");
            }
        });
    });


    $(".comment-form").submit(function(e) {
    e.preventDefault();
    var videoId = $(this).data("video");
    var text = $(this).find("input[name='text']").val();
    $.post("/comment/" + videoId, { text: text }, function(data) {
        // Appending new comment to the comments list
        $(".comments ul").append("<li>" + data.text + "</li>");
        // Clearing the comment input field
        $(e.target).find("input[name='text']").val("");
    });
    });
});