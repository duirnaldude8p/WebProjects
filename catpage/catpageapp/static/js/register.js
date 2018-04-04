
$(function(){
    $usr = $("#usrnm_in");
    $pwd = $('#pwd_in');
    $name = $('#name_in');
    $pic = $('#pic_in');
    $nav_list = $('#page_nav_list');
    is_verified = "false";

    function homeNavObject(){
        var new_home_nav =  '<li class="nav-item">\n'+
                                '<a class="nav-link" href="http://localhost:8000/catpageapp">Home</a>\n'+
                            '</li>';
        return new_home_nav;
    }
    function catlistNavObject(){
        var new_catlist_nav =   '<li class="nav-item">\n'+
                                    '<a class="nav-link" href="http://localhost:8000/catpageapp/catlist">See Cats</a>\n'+
                                '</li>';
        return new_catlist_nav;
    }
    function regNavObject(){
        var new_reg_nav =   '<li class="nav-item active">\n'+
                                '<a class="nav-link" href="http://localhost:8000/catpageapp/register">Register\n'+
                                    '<span class="sr-only">(current)</span>\n'+
                                '</a>\n'+
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
         is_set = false;
        
            if(is_verified==="true"){
                console.log("hello navbar");
                $nav_list.append(homeNavObject());
                $nav_list.append(catlistNavObject());
                $nav_list.append(accountNavObject());
                $nav_list.append(regNavObject());
                $nav_list.append(loginNavObject());
                is_set = true;
            }
        
        if(!is_set){
            $nav_list.append(homeNavObject());
            $nav_list.append(catlistNavObject());
            $nav_list.append(regNavObject());
            $nav_list.append(loginNavObject());
        }        
    }

    $.ajax({
        type: 'GET',
        url: '/catpageapp/getlogindata/',
        dataType: 'json',
        success: function(item){

            if(item[0]){
                is_verified = item[0].is_verified;
            }
            console.log("verify get success");
            createNavBar();
        },
        error:function(){
            console.log("verify get error");
        }
    });

    $("#reg_btn").on('click', function(e){
        e.preventDefault();
        var form_data = new FormData();
        form_data.append('username', $usr.val());
        form_data.append('password', $pwd.val());
        form_data.append('profile_pic', $pic.get(0).files[0]);
        form_data.append('account_name', $name.val());
        form_data.append('section', 'new');
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        //console.log("form datas: "+form_data.get("profile_pic"));
        $.ajax({
            type: 'POST',
            url: '../postaccountdata/',
            dataType: 'json',
            contentType: false,
            processData: false,
            data: form_data,
            cache: false,
            success: function(item){
                console.log("files: "+$pic.get(0).files+" - "+$pic.val()+" - "+form_data.get("profile_pic"));
                console.log('register post success: ');
                alert("Thank you "+$name.val()+" for registering");
            },
            error: function(){
                console.log("file: "+$pic.get(0).files+" - "+$pic.val()+" - "+form_data.get("profile_pic"));
                console.log('register post error');
                alert("Not registered")
            }         
        });  
    });
});
