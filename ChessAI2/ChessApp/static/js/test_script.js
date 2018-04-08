$(function(){

    $input = $('#input');
    $Btn = $('#button');
    $value = $('#textA');
    $op1 = $('#textB');
    $op2 = $('#textC');
    var hasStart = false;
    var hasGet = true;
    var hasPost = false;

    var chngble = localStorage.getItem("Changer");
    function updateable(){
    	chngble = localStorage.getItem("Changer");
    }
    setInterval(updateable, 1000);

 	var changr = new changer();
 	function updateGet(e){
 		//e.preventDefault();
 		if(!hasGet){
 			//console.log("get hasGet: "+hasGet+" chngble: "+chngble);
 			if(chngble=="Y"){
    			$.ajax({
        			type: 'GET',
        			dataType: 'json',
        			url: '/ChessApp/download_page/',
        			success: function(item){
        				//console.log("value: "+item.Changeable.Value);
        				//console.log("counter: "+item.Changeable.Counter);
                        //console.log("Get BinaryArray: "+item.Changeable.BinaryArray);
                        var bnar = item.Changeable.BinaryArray;
                        console.log("Get BinaryArray: "+bnar+' : '+bnar.length);
                        //console.log("hello");
                        localStorage.setItem("BinaryArray", bnar);
        				//console.log("changable: "+chngble);
       					changr.changeToN();
                        $value.text("Value: "+item.Changeable.Value);
                        $op1.text("Array: "+item.Changeable.BinaryArray);
     					//console.log("changable2: "+chngble);
        				hasGet = true;
      				},
      				error: function(){
      					console.log('post error');
      				}
 			    });
			}
		}
	}
   	setInterval(updateGet, 1000);

    function updatePost(e){
 		//e.preventDefault();
 		if(!hasStart||hasGet){
 			//console.log("hasGet: "+hasGet+" chngble: "+chngble);
 			if(chngble=="Y"){
 				var counter = localStorage.getItem("Counter");
 				counter = parseInt(counter);
                var binarr = localStorage.getItem("BinaryArray");
                //binarr = eval(binarr);
                console.log("post binarr: "+binarr+' : '+binarr.length);
        		$.ajax({
            		type: 'POST',
            		url: '/ChessApp/create_page/',
            		dataType: 'json',
            		data: {
                        bnryarr: binarr,
               			counter: counter,
                		csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                		section: 'Changeable'
            		},
            		success: function(item){
            			//console.log("post success");
                        $value.text("Value: "+item.Changeable.Value);
                        $op1.text("Array: "+item.Changeable.BinaryArray);
                        //console.log("post post BinaryArray: "+item.Changeable.BinaryArray);
            			hasGet = false;
        				hasStart = true;
            		},
            		error: function(){
                		console.log('post error');
            		}
        		});
        	}
        }
    }
    setInterval(updatePost, 1000);
});