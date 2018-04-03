$(function(){
	$usr = $('#usr_nm');
	$pwd = $('#pwd');
    $nav_list = $('#page_nav_list');
	
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
        var new_login_nav =   '<li class="nav-item active">\n'+
                                '<a class="nav-link" href="http://localhost:8000/catpageapp/login">Log In\n'+
                                    '<span class="sr-only">(current)</span>\n'+
                                '</a>\n'+
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

    $.ajax({
        type: 'GET',
        url: '/catpageapp/getlogindata/',
        dataType: 'json',
        success: function(item){
            is_verified = item[0].is_verified;
            console.log("verify get success");
            createNavBar();
        },
        error:function(){
            console.log("verify get error");
        }
    });

    $("#login_btn").on('click', function(e){
        e.preventDefault();
        var form_data = new FormData();
        form_data.append('username', $usr.val());
        form_data.append('password', $pwd.val());
        form_data.append('section', 'login');
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        $.ajax({
        	type: 'POST',
        	url: '/catpageapp/postlogindata/',
        	dataType: 'json',
        	contentType: false,
            processData: false,
            data: form_data,
            cache: false,
        	success: function(items){
        		console.log("login post success");
        	},
        	error:function(){
        		console.log("login post error");
        	}
    	});
    });
});