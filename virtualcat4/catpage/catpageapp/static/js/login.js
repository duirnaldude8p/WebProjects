$(function(){
	$usr = $('#usr_nm');
	$pwd = $('#pwd');

	$.ajax({
        type: 'GET',
        url: '/catpageapp/getaccountdata/',
        dataType: 'json',
        success: function(item){
        	console.log("login get success");
        	//console.log("usr :"+item[28].username);
        },
        error:function(){
        	console.log("login get error");
        }
    });
});