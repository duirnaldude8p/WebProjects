// $(function(){
// 	$prf_pic = $('#profile_pic_in');
//     $t_data = $('#t_text');
//     console.log("current_id: "+current_id);
//     // console.log("csrf: "+$('input[name=csrfmiddlewaretoken]').val());

//     // $("#submit_profile").on('click', function(e){
//     //     e.preventDefault();
//     //     var form_data = new FormData();
//     //     form_data.append('profile_pic', $prf_pic.get(0).files[0]);
//     //     form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
//     //     // console.log("yoo: ");
//     //     $.ajax({
//     //         type: 'PUT',
//     //         url: '/login_app/put_profile/'+current_id,
//     //         dataType: 'json',
//     //         contentType: false,
//     //         processData: false,
//     //         // data: 'csrfmiddlewaretoken='+$('input[name=csrfmiddlewaretoken]').val(),
//     //         data: "profile_pic=hello",
//     //         // beforeSend:function(xhr){
//     //         	// xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
//     //     	// },
//     //         cache: false,
//     //        	// beforeSend: function(xhr){xhr.setRequestHeader('X-CSRFToken', "{{csrf_token}}");},
//     //         success: function(){   
//     //             console.log('main post success: ');
//     //             // alert("comment successfully added");
//     //         },
//     //         error: function(){
//     //             console.log('main post error');
//     //             // alert("comment not added");
//     //         }         
//     //     });  
//     // });
//     $("#submit_profile").on('click', function(e){
//         e.preventDefault();
//         var form_data = new FormData();
//         form_data.append('profile_pic', $prf_pic.get(0).files[0]);
//         form_data.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val());
//     //     // console.log("yoo: ");
//         $.ajax({
//             type: 'PUT',
//             url: '/login_app/put_profile/'+current_id,
//             dataType: 'json',
//             contentType: false,
//             processData: false,
//             // data: "profile_pic=hello",
//             cache: false,
//             success: function(){   
//                 console.log('main post success: ');
//             },
//             error: function(){
//                 console.log('main post error');
//             }         
//         });  
//     });
// });