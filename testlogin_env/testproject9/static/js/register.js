$(function(){
	var $pic = $('#profile_pic_input');
	var $usrnm = $('#reg_usr');
	var $pwd = $('#reg_pwd');
    var form_data = null;
		
	
	$("#reg_submit").on('click', function(e){
        e.preventDefault();
		form_data = new FormData();
        // form_data.append('username', $usrnm.val());
        // form_data.append('password', $pwd.val());
        form_data.append('profile_pic', $pic.get(0).files[0]);
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        
        $.ajax({
        	type: 'POST',
        	url: '/login_app/postprofiledata/',
        	// dataType: 'json',
            contentType: false,
            processData: false,
            data: form_data,
            cache: false,
            success: function(){
            	console.log("post profile success");
            	alert("Your data has been entered");
            },
            error: function(){
            	console.log("post profile error");
            	alert("Sorry, Their appears to be an error entering your data");
            }
        });

	});

});