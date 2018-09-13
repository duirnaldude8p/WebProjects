$(function(){
	$pencilInput = $('#pencil_input');
	$penInput = $('#pen_input');
	$rubberInput = $('#rubber_input');
	$pic = $('#pic_input');

	form_data = new FormData();
    form_data.append('pencil', $pencilInput.val());
    form_data.append('pen', $penInput.val());
    form_data.append('rubber', $rubberInput.val());
    form_data.append('pic', $pic.get(0).files[0]);
    form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());

	$('#case_submit').on('click', function(e){
		e.preventDefault();
		$.ajax({
			type: 'POST',
			url: '/pencil_case_app/postcasedata/',
			cache: false,
            contentType: false,
            processData: false,
            data: form_data,
			success: function(){
				console.log("hello login_app formdata")
				alert("Post Successfull");
			},
			error: function(){
				alert("Post Unsuccessfull");
			}
		});
	});
});