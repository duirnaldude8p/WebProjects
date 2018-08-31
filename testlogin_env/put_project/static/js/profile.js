$(function(){
	$prf_pic = $('#profile_pic_update');
	// var user_id = "{{current_user_id}}";
	// console.log({{current_user_id|escapejs}});
	console.log("current_user_id: "+current_user_id);


    $("#submit_profile").on('click', function(e){
        e.preventDefault();
        $.ajax({
        	url: '/put_app/profile/' + current_user_id,
        	type: 'PUT',
        	data: JSON.stringify($prf_pic.get(0).files[0]),
        	headers: {
            	'x-auth-token': localStorage.accessToken,
            	"Content-Type": "application/json"
        	},
        	dataType: 'json'
		});
	});
});