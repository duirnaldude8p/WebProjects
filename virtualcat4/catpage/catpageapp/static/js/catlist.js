$(function(){
    $name = $("#name");
    $breed = $('#breed');
    $pic = $('#pic');
    $cat_text = $('#cat_text');
    var form = document.getElementById("cat_list_form");
    var is_verified = "false";
    //console.log("collapsssable");
    $("#cat_form_btn").on('click', function(e){
        e.preventDefault();
            
        var show = "form collapse.show card-body";
        var hide = "form collapse card-body";
        if(form.classList.contains('collapse.show')){
            form.className = "form collapse card-body";
        }else if(form.classList.contains('collapse')){
            form.className = "form collapse.show card-body";
        }     
    });

    $.ajax({
        type: 'GET',
        url: '/catpageapp/getlogindata/',
        dataType: 'json',
        success: function(item){
            is_verified = item[0].is_verified;

            console.log("catlist get success");
        },
        error:function(){
            console.log("catlist get error");
        }
    });

    $("#cat_submit_btn").on('click', function(e){
        e.preventDefault();
        console.log("hello");
        var form_data = new FormData();
        form_data.append('cat_name', $name.val());
        form_data.append('breed', $breed.val());
        form_data.append('story', $cat_text.val());
        form_data.append('cat_pic', $pic.get(0).files[0]);
        form_data.append('section', 'new');
        form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
        //console.log("form datas: "+form_data.get("profile_pic"));
        $.ajax({
            type: 'POST',
            url: '../postcatdata/',
            dataType: 'json',
            contentType: false,
            processData: false,
            data: form_data,
            success: function(item){
                console.log("files: "+$pic.get(0).files+" - "+$pic.val()+" - "+form_data.get("profile_pic"));
                console.log('catlist post success: ');
            },
            error: function(){
                console.log("file: "+$pic.get(0).files+" - "+$pic.val()+" - "+form_data.get("profile_pic"));
                console.log('catlist post error');
            }         
        });  
    });
});
