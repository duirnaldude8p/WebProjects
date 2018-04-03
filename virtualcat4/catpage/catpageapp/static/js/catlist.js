function getCatPage(myid){
    var cat_id = myid;
    console.log("my id: "+myid);
    localStorage.setItem("cat id", cat_id);
    window.location.href = "http://localhost:8000/catpageapp/catpage/";
}
    

$(function(){
    $name = $("#name");
    $breed = $('#breed');
    $pic = $('#pic');
    $cat_text = $('#cat_text');
    $list = $("#cat_list_objects");
    var form = document.getElementById("cat_list_form");
    var is_verified = "false";
    var id_count = 0;
    $nav_list = $('#page_nav_list');
    //console.log("collapsssable");


    function objectListItem(myid, image, name){
        var new_object =    '<li>\n'+
                                '<div id="cat_image'+myid+'" class="image_rectangle" onclick="getCatPage('+myid+')">\n'+
                                    '<img class="cat_image img-fluid" src="'+image+'" alt="">\n'+
                                    '<div class="centered">'+name+'</div>\n'+
                                '</div>\n'+
                                '<hr>\n'+
                            '</li>';
        return new_object;
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


    $("#cat_form_btn").on('click', function(e){
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
            createNavBar();
        },
        error:function(){
            console.log("catlist get error");
        }
    });
    
    function getcats(){
        $.ajax({
            type: 'GET',
            url: '/catpageapp/getcatdata/',
            dataType: 'json',
            success: function(items){
                var mycats = items;
        

                console.log("cats - "+mycats);
                $.each(mycats, function(i, val){
                    var myurl = "http://localhost:8000/";
                    var image = val.cat_pic;
                    var mystring = image.substring(0,11);
                    var mystring2 = image.replace(mystring, "");
                    myurl = myurl+mystring2;
                    console.log("my url: "+myurl);
                    $list.append(objectListItem(val.id, myurl, val.cat_name));
                });

                console.log("catlist get success");
            },
            error:function(){
                console.log("catlist get error");
            }
        });
    }
    getcats();

    function getlastcat(){
        $.ajax({
            type: 'GET',
            url: '/catpageapp/getcatdata/',
            dataType: 'json',
            success: function(items){
                var mycats = items;
                console.log("item length: "+items.length);
                my_item = items[items.length-1];
                    
                var myurl = "http://localhost:8000/";
                var image = my_item.cat_pic;
                var mystring = image.substring(0,11);
                var mystring2 = image.replace(mystring, "");
                myurl = myurl+mystring2;
                console.log("my url: "+myurl);
                $list.append(objectListItem(my_item.id, myurl, my_item.cat_name));
                console.log("catlist get success");
            },
            error:function(){
                console.log("catlist get error");
            }
        });
    }

    $("#cat_submit_btn").on('click', function(e){
        e.preventDefault();
        console.log("hello");
        var form_data = new FormData();
        form_data.append('cat_name', $name.val());
        form_data.append('breed', $breed.val());
        form_data.append('story', $cat_text.val());
        form_data.append('cat_pic', $pic.get(0).files[0]);
        form_data.append('section', 'update cats');
        form_data.append('get_id', 24);
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        //console.log("form datas: "+form_data.get("profile_pic"));
        if(is_verified==="true"){
            $.ajax({
                type: 'POST',
                url: '../postmaindata/',
                dataType: 'json',
                contentType: false,
                processData: false,
                data: form_data,
                cache: false,
                success: function(item){
                    console.log('catlists post success: ');
                    getlastcat();
                },
                error: function(){
                    console.log('catlist post error');
                }         
            });
        }else{
            alert("no account verified");
        }  
    });

});
