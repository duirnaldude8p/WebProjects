
$(function(){
    $usr = $("#usrnm_in");
    $pwd = $('#pwd_in');
    $name = $('#name_in');
    $pic = $('#pic_in');


    $("#reg_btn").on('click', function(e){
        e.preventDefault();
        var form_data = new FormData();
        form_data.append('username', $usr.val());
        form_data.append('password', $pwd.val());
        form_data.append('account_name', $name.val());
        form_data.append('profile_pic', $pic.get(0).files[0]);
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
            success: function(item){
                console.log("files: "+$pic.get(0).files+" - "+$pic.val()+" - "+form_data.get("profile_pic"));
                console.log('register post success: ');
            },
            error: function(){
                console.log("file: "+$pic.get(0).files+" - "+$pic.val()+" - "+form_data.get("profile_pic"));
                console.log('register post error');
            }         
        });  
    });
});
