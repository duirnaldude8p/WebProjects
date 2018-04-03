$(function(){
	$usr = $('#usr_nm');
	$pwd = $('#pwd');
	
    
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