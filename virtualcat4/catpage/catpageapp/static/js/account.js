
$(function(){
    $name = $("#account_name");
    $email = $('#account_email');
    $pic = $('#account_image_container');
    $new_pic = $('#pic_in');
    var form = document.getElementById("pic_form");
    var is_verified = "false";
    var id_count = 0;
    var login_id = 0;
    var account_id = 0;
    //console.log("collapsssable");

    function objectPictureItem(image){
        var new_picture =  '<img id="account_image"\n'+ 
                           'class="card-img-top img-fluid"\n'+ 
                           'src="'+image+'"\n'+
                           'alt="http://placehold.it/1200x500">';   
        return new_picture;
    }


    $.ajax({
        type: 'GET',
        url: '/catpageapp/getlogindata/',
        dataType: 'json',
        cache: false,
        success: function(item){
            is_verified = item[0].is_verified;
            name = item[0].account_name;
            email = item[0].username;
            pic = item[0].profile_pic;
            login_id = item[0].id;
            account_id = item[0].current_id;

            var my_url = "http://localhost:8000/";
            var my_string = pic.substring(0,11);
            var my_string2 = pic.replace(my_string, "");
            my_url = my_url+my_string2;
            $pic.html(objectPictureItem(my_url));
            $name.text("Name: "+name);
            $email.text("Email: "+email);
            console.log("is_verified: "+is_verified);
            console.log("account get success");
        },
        error:function(){
            console.log("account get error");
        }
    });

    function changepicture(){
        $.ajax({
        type: 'GET',
        url: '/catpageapp/getlogindata/',
        dataType: 'json',
        cache: false,
        success: function(item){
            new_pic = item[0].profile_pic;

            var my_url = "http://localhost:8000/";
            var my_string = new_pic.substring(0,11);
            var my_string2 = new_pic.replace(my_string, "");
            my_url = my_url+my_string2;
            $pic.html(objectPictureItem(my_url));
            console.log("is_verified: "+is_verified);
            console.log("account get success");
        },
        error:function(){
            console.log("account get error");
        }
    });   
    }
    
    
    $("#pic_btn").on('click', function(e){
        e.preventDefault();

        console.log("my picture: "+$new_pic.get(0).files[0]);
        
        var form_data = new FormData();
        form_data.append('get_id', login_id);
        form_data.append('current_id', account_id);
        form_data.append('profile_pic', $new_pic.get(0).files[0]);
        form_data.append('section', 'update picture');
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
                console.log("login: "+login_id);
                console.log("current id: "+account_id);
                changepicture();
                console.log("account post success");
            },
            error:function(){
                console.log("account post error");
            }
        });

        var form_data2 = new FormData();
        form_data2.append('get_id', account_id);
        form_data2.append('profile_pic', $new_pic.get(0).files[0]);
        form_data2.append('section', 'update picture');
        form_data2.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        $.ajax({
            type: 'POST',
            url: '/catpageapp/postaccountdata/',
            dataType: 'json',
            contentType: false,
            processData: false,
            data: form_data2,
            cache: false,
            success: function(items){
                console.log("account post success");
            },
            error:function(){
                console.log("account post error");
            }
        });
    });   
});
