$(function(){
	$list = $('#case_list');
 	var data_isrecieved = false;
 	var current_id = 0;
 	var data = 0;
 	$currentPencil = null;
 	$currentPen = null;
 	$currentRubber = null;


 	

	function objectListItem(myid, pencil, rubber, pen){
        var pencilcase_object =   
        		'<div id="case_form'+myid+'" class="row container post-box" method="post" action="">\n'+
					'<div class="col">\n'+
						'Add Pencil Case\n'+
					'</div>\n'+
					'<div class="w-100"></div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'Pencil:\n'+ 
					'</div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'<div id="pencil_text" style="display: initial">\n'+
							pencil+
						'</div>\n'+
						'<div style="display: none" class="width-max height-max">\n'+
							'<input  id="pencil_input'+myid+'" type="text"  class="width-max">\n'+
						'</div>\n'+
					'</div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'<button id="pencil_button'+myid+'" class="pcc-button">Update</button>\n'+
					'</div>\n'+
					'<div class="w-100"></div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'Rubber:\n'+
					'</div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'<div id="rubber_text" style="display: initial">\n'+
							rubber+
						'</div>\n'+
						'<div style="display: none" class="width-max">\n'+
							'<input id="rubber_input'+myid+'" type="text" class="width-max height-max">\n'+
						'</div>\n'+
					'</div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'<button id="rubber_button'+myid+'" class="pcc-button">Update</button>\n'+
					'</div>\n'+
					'<div class="w-100"></div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'Pen:\n'+
					'</div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'<div id="pen_text" style="display: initial">\n'+
							pen+
						'</div>\n'+
						'<div style="display: none" class="width-max">\n'+
							'<input id="pencil_input'+myid+'" type="text" class="width-max">\n'+
						'</div>\n'+
					'</div>\n'+
					'<div class="col col-xl-4 col-lg-4 col-md-4 col-sm-4">\n'+
						'<button id="pen_button'+myid+'" class="pcc-button">Update</button>\n'+
					'</div>\n'+
				'</div>';
        return pencilcase_object;
    }

	$.ajax({
		type: 'GET',
		url: '/pencil_case_app/getcasedata/',
		cache: false,
		success: function(items){
			console.log("Get Success "+items[0].pencil);
			$('#pencil_text').text(items[0].pencil);
			$('#pen_text').text(items[0].pen);
			$('#rubber_text').text(items[0].rubber);
			$.each(items, function(i, item){
				$list.append(objectListItem(item.id, item.pencil, item.rubber, item.pen));
			});
			data = items;
			data_recieved = true;
		},
		error: function(){
			console.log("Get Error");
		}
	});

	function sendPutRequests(){

 		if(data_recieved == true){
 			$.each(data, function(i, item){
 				$('#pencil_button'+item.id).on('click', function(e){
 					e.preventDefault();
 					$currentPencil = $('#pencil_input'+item.id);
 					$.ajax({
 						type: 'PUT',
 						url: '/pencil_case_app/putcasedata/'+item.id,
 						data: 'pencil='+$currentPencil.val(),
 						success: function(){
 							console.log("pencil put success");
 						},
 						error: function(){
 							console.log("pencil put error");
 						}
 					});
 				});
 				$('#rubber_button'+item.id).on('click', function(e){
 					e.preventDefault();
 					$currentRubber = $('#rubber_input'+item.id);
 					$.ajax({
 						type: 'PUT',
 						url: '/pencil_case_app/putcasedata/'+item.id,
 						data: 'rubber='+$currentRubber.val(),
 						success: function(){
 							console.log("rubber put success");
 						},
 						error: function(){
 							console.log("rubber put error");
 						}
 					});
 				});
				$('#pen_button'+item.id).on('click', function(e){
 					e.preventDefault();
 					$currentPen = $('#pen_input'+item.id);
 					$.ajax({
 						type: 'PUT',
 						url: '/pencil_case_app/putcasedata/'+item.id,
 						data: 'pen='+$currentPen.val(),
 						success: function(){
 							console.log("pen put success");
 						},
 						error: function(){
 							console.log("pen put error");
 						}
 					});
 				});
			});
 		}
 	}

 	setInterval(sendPutRequests, 500);
});