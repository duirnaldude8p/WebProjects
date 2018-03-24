
$(function(){
    $usr = $("#usrnm_in");
    $pwd = $('#pwd_in');
    $name = $('#name_in');
    $pic = $('#pic_in');
    // $reg_btn = $('#reg_btn');
   
    // $.ajax({
    //     type: 'GET',
    //     dataType: 'json',
    //     url: '/testApp/download/',
    //     success: function(value){
    //         console.log("get register sucess");
                   
    //     },
    //     error: function(){
    //         console.log('get register error');
    //     }
    // });

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
                    profile_pic: $pic.val(),
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    section:"new"
            },
            success: function(item){
                console.log('register post success: ');
            },
            error: function(){
                console.log('register post error');
            }         
        });  
    });
});
