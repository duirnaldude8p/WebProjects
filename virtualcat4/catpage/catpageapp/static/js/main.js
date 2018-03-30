$(function(){
    $text = $('#comment_text');
    $list = $("#home_page_comments");
    var form = document.getElementById("main_comment_form");
    var is_verified = "false";
    var name = '';
    var pic = null;
    

    function commentListItem(comment, image, name){
        var new_comment = '<li>\n'+
            '<div class="card-pic" >\n'+
                '<div class="image_circle">\n'+
                    '<img class="my_image img-fluid" src="'+image+'"  alt="">\n'+
                '</div>\n'+
            '</div>\n'+
            '<small class="text-muted soft_text">'+name+'</small>\n'+
            '<div class="card-comment">\n'+
                '<p>'+comment+'</p>\n'+
            '</div>\n'+
            '<hr>\n'+
        '</li>';
        return new_comment;
    }

    $("#main_comment_form_btn").on('click', function(e){
        e.preventDefault();
            
        var show = "form collapse.show card-body";
        var hide = "form collapse card-body";
        if(form.classList.contains('collapse.show')){
            form.className = "form collapse card-body";
        }else if(form.classList.contains('collapse')){
            form.className = "form collapse.show card-body";
        }     
    });

    $.ajax({
        type: 'GET',
        url: '/catpageapp/getlogindata/',
        dataType: 'json',
        success: function(item){
            is_verified = item[0].is_verified;
            name = item[0].account_name;
            pic = item[0].profile_pic;
            //console.log("pic: "+pic);
            console.log("verify get success");
        },
        error:function(){
            console.log("verify get error");
        }
    });

    $.ajax({
        type: 'GET',
        url: '/catpageapp/getmaindata/',
        dataType: 'json',
        success: function(item){
            //console.log("items: "+item[0].comments);
            var mycomments = item[0].comments;
            mycomments = mycomments.replace(/'/g, '"');
            mycomments = JSON.parse(mycomments);
           
            $.each(mycomments, function(i, val){
                var myurl = "http://localhost:8000/";
                var image = val.comment.picture
                var mystring = image.substring(0,11);
                var mystring2 = image.replace(mystring, "");
                myurl = myurl+mystring2;
                //console.log("my url: "+myurl);
                //console.log("comments: "+commentListItem(val.comment.comm, myurl, val.comment.name));
                $list.append(commentListItem(val.comment.comm, myurl, val.comment.name));
            });
            console.log("main get success");
        },
        error:function(){
            console.log("main get error");
        }
    });
    
    //id of the only main object should be one but can check in getmaindata
    $("#main_submit_comment_btn").on('click', function(e){
        e.preventDefault();
        var form_data = new FormData();
        form_data.append('comments', $text.val());
        form_data.append('name', name);
        form_data.append('picture', pic);
        form_data.append('get_id', 4);
        form_data.append('section', 'update comments');
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        $.ajax({
            type: 'POST',
            url: '/catpageapp/postmaindata/',
            dataType: 'json',
            contentType: false,
            processData: false,
            data: form_data,
            success: function(item){
                var myurl = "http://localhost:8000/";
                var image = pic
                var mystring = image.substring(0,11);
                var mystring2 = image.replace(mystring, "");
                myurl = myurl+mystring2;
                //console.log("my url: "+myurl);
                //console.log("commments: "+commentListItem(, myurl, val.comment.name));
                $list.append(commentListItem($text.val(), myurl, name));
                console.log('main post success: ');
            },
            error: function(){
                console.log('main post error');
            }         
        });  
    });
});
