$(function(){
	// var $pic = $('#profile_pic_input');
	var $usrnm = $('#reg_usr');
	var $pwd = $('#reg_pwd');
    // var form_data = null;

    form_data = new FormData();
    form_data.append('username', $usrnm.val());
    form_data.append('password', $pwd.val());
    // form_data.append('profile_pic', $pic.get(0).files[0]);
    form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
	// console.log("hello csrf "+$('input[name=csrfmiddlewaretoken]').val());
    
	
	$("#reg_submit").on('click', function(e){
        e.preventDefault();
        $.ajax({
        	method: 'POST',
        	url: '/login_app/postprofiledata/',
        	// dataType: 'json',
            // contentType: false,
            // processData: false,
            // data: form_data,
            // cache: false,
            data:{
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                username: $usrnm.val(),
                password: $pwd.val(),
            },
            success: function(item){
                // console.log("options success");
            	console.log("get profile success");
            	alert("Your data has been recieved");
            },
            error: function(){
                // console.log("options faliure");
            	console.log("get profile error");
            	alert("Sorry, Their appears to be an error getting your data");
                console.log("hello user "+$usrnm.val());
                console.log("hello password "+$pwd.val());
                // console.log("hello pic "+$pic.get(0).files[0]);
    
            }
        });

	});

    // $("#reg_submit2").on('click', function(e){
    //     e.preventDefault();
    //     $.ajax({
    //         type: 'POST',
    //         url: '/login_app/postprofiledata2/',
    //         // contentType: false,
    //         // processData: false,
    //         // data: form_data,
    //         // cache: false,
    //         success: function(item){
    //             console.log("get profile success");
    //             alert("Your data has been recieved");
    //         },
    //         error: function(){
    //             console.log("get profile error");
    //             alert("Sorry, Their appears to be an error getting your data");
    //         }
    //     });

    // });

});