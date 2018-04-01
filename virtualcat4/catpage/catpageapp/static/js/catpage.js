$(function(){
   
    $list = $("#cat_page_comments");
    var form = document.getElementById("cat_form");
    var is_verified = "false";
    var current_cat_id = 58;
    var current_cat_place = 0;
    var id_found = false;
    $cat_details = $('#cat_page_details');

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

    function catDetailsItem(title, image, breed, text){
        var new_details = '<img class="card-img-top img-fluid" src="'+image+'" alt="">\n'+
                '<div class="card-body">\n'+
                    '<h3 class="card-title">'+title+'</h3>\n'+
                    '<p class="card-text">Breed:'+breed+'</p>\n'+
                    '<p class="card-text">'+text+'</p>\n'+
                '</div>';
        return new_details;
    }

    $("#catpage_comment_btn").on('click', function(e){
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
            console.log("is_verified: "+is_verified);
            console.log("catlist get success");
        },
        error:function(){
            console.log("catlist get error");
        }
    });

    $.ajax({
        type: 'GET',
        url: '/catpageapp/getmaindata/',
        dataType: 'json',
        success: function(item){
            //console.log("items: "+item[0].comments);
            var myids = item[0].my_cat_id;
            console.log("ids: "+myids);
            myids = myids.replace(/'/g, '"');
            myids = JSON.parse(myids);
           
            $.each(myids, function(i, val){
                //console.log("id vals: "+val);
                if(current_cat_id==val){
                    console.log("id found val: "+val+' - '+i);
                    id_found = true;
                    current_cat_place = i;
                }
            });
            if(id_found){
                getcatpage();
            }
            console.log("main get success");
        },
        error:function(){
            console.log("main get error");
        }
    });

    function getcatpage(){
        if(is_verified=="true"&&id_found){
            
            $.ajax({
                type: 'GET',
                url: '/catpageapp/getcatdata/',
                dataType: 'json',
                success: function(items){
                    //console.log("items: "+item[0].comments);
                    my_cat_place = current_cat_place;
                    console.log("cat stuff: "+items[current_cat_place].cat_name);
                    // var my_title = items[my_cat_id].cat_name;
                    // var my_text =  items[my_cat_id].story;
                    // var my_image =  items[my_cat_id].cat_pic;
                    // var my_breed =  items[my_cat_id].breed;
                    // console.log("cat info: "+my_title+' - '+my_image+' - '+my_breed+' - '+my_test);
                    // $cat_details.append(catDetailsItem(my_title, my_image, my_breed, my_test));
                //     console.log("ids: "+myids);
                //     myids = myids.replace(/'/g, '"');
                //     mycomments = JSON.parse(mycomments);
           
                //     $.each(mycomments, function(i, val){
                //     var myurl = "http://localhost:8000/";
                //     var image = val.comment.picture
                //     var mystring = image.substring(0,11);
                //     var mystring2 = image.replace(mystring, "");
                //     myurl = myurl+mystring2;
                //     //console.log("my url: "+myurl);
                //     //console.log("comments: "+commentListItem(val.comment.comm, myurl, val.comment.name));
                //     $list.append(commentListItem(val.comment.comm, myurl, val.comment.name));
                // });
                console.log("main get success");
                },
                error:function(){
                    console.log("main get error");
                }
            });
        }else{
            alert("error no data");
        }  
    }

    // $.ajax({
    //     type: 'GET',
    //     url: '/catpageapp/getlogindata/',
    //     dataType: 'json',
    //     success: function(item){
    //         is_verified = item[0].is_verified;
    //         name = item[0].account_name;
    //         pic = item[0].profile_pic;
    //         //console.log("pic: "+pic);
    //         console.log("verify get success");
    //     },
    //     error:function(){
    //         console.log("verify get error");
    //     }
    // });

    // $.ajax({
    //     type: 'GET',
    //     url: '/catpageapp/getmaindata/',
    //     dataType: 'json',
    //     success: function(item){
    //         //console.log("items: "+item[0].comments);
    //         var mycomments = item[0].comments;
    //         mycomments = mycomments.replace(/'/g, '"');
    //         mycomments = JSON.parse(mycomments);
           
    //         $.each(mycomments, function(i, val){
    //             var myurl = "http://localhost:8000/";
    //             var image = val.comment.picture
    //             var mystring = image.substring(0,11);
    //             var mystring2 = image.replace(mystring, "");
    //             myurl = myurl+mystring2;
    //             //console.log("my url: "+myurl);
    //             //console.log("comments: "+commentListItem(val.comment.comm, myurl, val.comment.name));
    //             $list.append(commentListItem(val.comment.comm, myurl, val.comment.name));
    //         });
    //         console.log("main get success");
    //     },
    //     error:function(){
    //         console.log("main get error");
    //     }
    // });
    
    // //id of the only main object should be one but can check in getmaindata
    // $("#main_submit_comment_btn").on('click', function(e){
    //     e.preventDefault();
    //     var form_data = new FormData();
    //     form_data.append('comments', $text.val());
    //     form_data.append('name', name);
    //     form_data.append('picture', pic);
    //     form_data.append('get_id', 8);
    //     form_data.append('section', 'update comments');
    //     form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
    //     $.ajax({
    //         type: 'POST',
    //         url: '/catpageapp/postmaindata/',
    //         dataType: 'json',
    //         contentType: false,
    //         processData: false,
    //         data: form_data,
    //         success: function(item){
    //             var myurl = "http://localhost:8000/";
    //             var image = pic
    //             var mystring = image.substring(0,11);
    //             var mystring2 = image.replace(mystring, "");
    //             myurl = myurl+mystring2;
    //             //console.log("my url: "+myurl);
    //             //console.log("commments: "+commentListItem(, myurl, val.comment.name));
    //             $list.append(commentListItem($text.val(), myurl, name));
    //             console.log('main post success: ');
    //         },
    //         error: function(){
    //             console.log('main post error');
    //         }         
    //     });  
    // });
});
