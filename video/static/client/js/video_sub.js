$('#comment-submit').click(function(){
    var content = $('#comment-content').val();
    var csrfToken = $('#django-csrf-token').val();
    var videoId =  $('#comment-content').attr('data-video-id');
    var userId = $('#comment-content').attr('data-user-id');
    var url = $(this).attr('data-url');

    if (!content){
        alert('评论不能为空~');
        return;
    };
    $.ajax({
        url: url,
        type: 'post',
        data: {
            content: content,
            videoId: videoId,
            userId: userId,
            csrfmiddlewaretoken: csrfToken
        },
        success: function(data){
            if (data.code){
                alert(data.msg)
            }
        },
        fail: function(e){
            console.log(e);
        }
    });
});