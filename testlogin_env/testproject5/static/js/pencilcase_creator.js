$(function(){
	$pencilInput = $('#pencil_input');
	$penInput = $('#pen_input');
	$rubberInput = $('#rubber_input');

	$('#case_submit').on('click', function(e){
		e.preventDefault();
		$.ajax({
			type: 'POST',
			url: '/pencil_case_app/postcasedata/',
			cache: false,
			data: {
				'pencil': $pencilInput.val(),
				'pen': $penInput.val(),
				'rubber': $rubberInput.val(),
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function(){
				alert("Post Successfull");
			},
			error: function(){
				alert("Post Unsuccessfull");
			}
		});
	});
});