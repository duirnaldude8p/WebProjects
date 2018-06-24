$(function(){
	$sq_box = $("#square-box");
	$square = $(".square");
	$img = $(".my_image");
	
	var imgHeight = $img.height();
	var imgWidth = $img.width();
	var sqHeight = $sq_box.height();
	var sqWidth = $sq_box.width();
	
	
	if(sqHeight<sqWidth){
		$square.css('height', sqHeight+'px');
		$square.css('width', sqHeight+'px');
	}else{
		$square.css('height', sqWidth+'px');
		$square.css('width', sqWidth+'px');
	}



})