
$(function(){
    $usr = $("#usrnm_in");
    $pwd = $('#pwd_in');
    $name = $('#name_in');
    $pic = $('#pic_in');


    $("#reg_btn").on('click', function(e){
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '../postaccountdata/',
            dataType: 'json',
            //contentType: "application/json; charset=utf-8",
            data:{
                    username: $usr.val(),
                    password: $pwd.val(),
                    account_name: $name.val(),
                    profile_pic: $pic.get(0).files,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    section:"new"
            },
            success: function(item){
                console.log("files: "+$pic.get(0).files+" - "+$pic.val());
                console.log('register post success: ');
            },
            error: function(){
                console.log("file: "+$pic.get(0).files+" - "+$pic.val());
                console.log('register post error');
            }         
        });  
    });
});
