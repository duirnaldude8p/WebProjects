$('#button').on('click', function(e){
	//console.log(" hello onclick");
	var item = localStorage.getItem("Changer");
	if(item=="N"){
		localStorage.setItem("Changer", "Y");
		var counter = localStorage.getItem("Counter");
		counter = parseInt(counter);
		counter = counter + 1;
		localStorage.setItem("Counter", counter);
		var binarr = localStorage.getItem("BinaryArray");
		console.log("binarrA: "+binarr+' '+binarr.length);
		//binarr = JSON.stringify(binarr);
		binarr = eval(binarr);
		//binarr = eval(binarr);
		//console.log("binarrB: "+binarr+' '+binarr.length);
		if(binarr[2]==1){
			binarr[2] = 0;
			binarr[1] = 1;
		}
		//console.log("binarrC: "+binarr+' '+binarr.length);
		console.log("on click string bin: "+JSON.stringify(binarr)+' - '+JSON.stringify(binarr).length);
		localStorage.setItem("BinaryArray", JSON.stringify(binarr));
	}	
});	
