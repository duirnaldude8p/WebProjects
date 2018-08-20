// $(function(){
// 	$prf_pic = $('#profile_pic_in');
//     $t_data = $('#t_text');
	
//     // $("#submit_profile").on('click', function(e){
//     //     e.preventDefault();
//     //     var form_data = new FormData();
//     //     form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
//     //     form_data.append('profile_pic', $prf_pic.get(0).files[0]);
//     //     form_data.append('section', 'profile');
//     //     // console.log("form", form_data);
//     //     $.ajax({
//     //     	type: 'PUT',
//     //     	url: '/login_app/profile/',
//     //     	dataType: 'json',
//     //     	contentType: false,
//     //         processData: false,
//     //         data: {'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
//     //         cache: false,
//     //     	success: function(items){
//     //     		console.log("login put success");
//     //             // alert("Thanks for entering your info check account to see if logged in");
//     //     	},
//     //     	error:function(){
//     //     		console.log("login put error");
//     //             // alert("Log In Error");
//     //     	}
//     // 	});
//     // });
//     $("#submit_profile").on('click', function(e){
//         e.preventDefault();
//         // var form_data = new FormData();
//         // form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
//         // form_data.append('profile_pic', $prf_pic.get(0).files[0]);
//         // form_data.append('section', 'profile');
//         // // console.log("form", form_data);
//         $.ajax({
//             type: 'POST',
//             url: '/login_app/profile/',
//             dataType: 'json',
//             // contentType: false,
//             // processData: false,
//             data: { 
//                     'test_data': $t_data.val(),
//                     'username':'1',
//                     'user':'1',
//                     'section': 'test post',
//                     'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
//             },
//             // cache: false,
//             success: function(items){
//                 console.log("login put success");
//                 // alert("Thanks for entering your info check account to see if logged in");
//             },
//             error:function(){
//                 console.log("login put error");
//                 // alert("Log In Error");
//             }
//         });
//     });
// });