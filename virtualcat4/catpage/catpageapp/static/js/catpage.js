$(function(){
   
    $list = $("#cat_page_comments");
    var form = document.getElementById("cat_form");
    var is_verified = "false";
    var current_cat_place = 0;
    var main_cat_id_found = false;
    var cat_id_found = false;
    $cat_details = $('#cat_page_details');
    $text = $('#comment_text');
    var name = '';
    var pic = '';
    var recieved_list_cat_id = localStorage.getItem('cat id')
    var current_cat_id = parseInt(recieved_list_cat_id);
    $nav_list = $('#page_nav_list');


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
                    '<p class="card-text">Breed: '+breed+'</p>\n'+
                    '<p class="card-text">Story: '+text+'</p>\n'+
                '</div>';
        return new_details;
    }

    function homeNavObject(){
        var new_home_nav =  '<li class="nav-item">\n'+
                                '<a class="nav-link" href="http://localhost:8000/catpageapp">Home</a>\n'+
                            '</li>';
        return new_home_nav;
    }
    function catlistNavObject(){
        var new_catlist_nav =   '<li class="nav-item active">\n'+
                                    '<a class="nav-link" href="http://localhost:8000/catpageapp/catlist">See Cats\n'+
                                        '<span class="sr-only">(current)</span>\n'+
                                    '</a>\n'+
                                '</li>';
        return new_catlist_nav;
    }
    function regNavObject(){
        var new_reg_nav =   '<li class="nav-item">\n'+
                                '<a class="nav-link" href="http://localhost:8000/catpageapp/register">Register</a>\n'+
                            '</li>';
        return new_reg_nav;
    }
    function accountNavObject(){
        var new_account_nav =   '<li class="nav-item">\n'+
                                    '<a class="nav-link" href="http://localhost:8000/catpageapp/account">Account</a>\n'+
                                '</li>';
        return new_account_nav;
    }
    function loginNavObject(){
        var new_login_nav =   '<li class="nav-item">\n'+
                                '<a class="nav-link" href="http://localhost:8000/catpageapp/login">Log In</a>\n'+
                            '</li>';
        return new_login_nav;
    }

    function createNavBar(){
        // console.log("my is_verified: "+is_verified);
        if(is_verified==="true"){
            console.log("hello navbar");
            $nav_list.append(homeNavObject());
            $nav_list.append(catlistNavObject());
            $nav_list.append(accountNavObject());
            $nav_list.append(loginNavObject());
        }else{
            $nav_list.append(homeNavObject());
            $nav_list.append(catlistNavObject());
            $nav_list.append(regNavObject());
            $nav_list.append(loginNavObject());
        }   
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
            name = item[0].account_name;
            pic = item[0].profile_pic;
            console.log("is_verified: "+is_verified);
            console.log("catlist get success");
            createNavBar();
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
                    console.log("id found val: "+val);
                    main_cat_id_found = true;
                    return false;
                }
            });
            if(main_cat_id_found&&is_verified=="true"){
                getcatpage();
            }
            console.log("main get success");
        },
        error:function(){
            console.log("main get error");
        }
    });

    function getcatpage(){
        if(is_verified=="true"){
            
            $.ajax({
                type: 'GET',
                url: '/catpageapp/getcatdata/',
                dataType: 'json',
                success: function(items){
                    //console.log("items: "+item[0].comments);
                    my_cats = items;
                    my_cat_place = current_cat_place;
                    my_cat_id = current_cat_id; 
                    my_item = null;
                    // console.log("cat stuff: "+items[current_cat_place].cat_name);
                    $.each(my_cats, function(i, val){
                        var next_id = val.id;
                        if(next_id==current_cat_id){
                            console.log("cat id found: "+val.id+' - '+i);
                            cat_id_found = true;
                            my_cat_place = i;
                            return false;
                        }
                    });

                    if(cat_id_found){
                        var my_title = items[my_cat_place].cat_name;
                        var my_text =  items[my_cat_place].story;
                        var my_image =  items[my_cat_place].cat_pic;
                        var my_breed =  items[my_cat_place].breed;
                        //console.log("cat info: "+my_title+' - '+my_image+' - '+my_breed+' - '+my_text);
                        var my_cat_url = "http://localhost:8000/";
                        var my_string = my_image.substring(0,11);
                        var my_string2 = my_image.replace(my_string, "");
                        my_cat_url = my_cat_url+my_string2;
                        $cat_details.append(catDetailsItem(my_title, my_cat_url, my_breed, my_text));

                        var my_cat_comments =  items[my_cat_place].cat_comments;
                        my_cat_comments = my_cat_comments.replace(/'/g, '"');
                        my_cat_comments = JSON.parse(my_cat_comments);

                        $.each(my_cat_comments, function(i, val){
                            console.log("cat comments: "+val.cat_comment.picture);
                            var myurl = "http://localhost:8000/";
                            var image = val.cat_comment.picture
                            var mystring = image.substring(0,11);
                            var mystring2 = image.replace(mystring, "");
                            myurl = myurl+mystring2;
                            //console.log("my url: "+myurl);
                            //console.log("comments: "+commentListItem(val.comment.comm, myurl, val.comment.name));
                             $list.append(commentListItem(val.cat_comment.comm, myurl, val.cat_comment.name));
                        });
                    }
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

    $("#cat_comment_form_btn").on('click', function(e){
        e.preventDefault();
        var form_data = new FormData();
        form_data.append('cat_comments', $text.val());
        form_data.append('name', name);
        form_data.append('picture', pic);
        form_data.append('get_id', current_cat_id);
        form_data.append('section', 'update comments');
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        console.log("yoo: ");
        $.ajax({
            type: 'POST',
            url: '/catpageapp/postcatdata/',
            dataType: 'json',
            contentType: false,
            processData: false,
            data: form_data,
            cache: false,
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
