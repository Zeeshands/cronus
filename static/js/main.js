(function($){
	'use strict';
	
	jQuery(document).ready(function(){
 var audio;
        function formatAMPM(date) {
            var hours = date.getHours();
            console.log(hours);
            var minutes = date.getMinutes();
            var ampm = hours >= 12 ? 'pm' : 'am';
            // hours = hours % 12;
            // hours = hours ? hours : 12; // the hour '0' should be '12'
            minutes = minutes < 10 ? '0'+minutes : minutes;
            var strTime = hours + ':' + minutes + ' ' + ampm;
            return strTime;
          }

          var i = 0;
          var msg;
          function chat(msg) {
              $.get("http://151.253.132.135:9000/cronus",
                  {
                    field: msg,
                  }).done(function (data_get) {
                      i++
                      console.log(data_get);
                      $('.lds-ellipsis').hide();
                      var user_msg = ' <div class="user_msg">'+
                          '<img src="../static/images/female_avatar.jpg" class="pull-right user-img">'+
     
                          '<div class="msj-rta macro">'+ 
                          '<a class="play-pause-button fa fa-play" data-id="'+i+'"></a>'+
  
                                  '<div class="text text-r">'+ 
                                      // '<p>User '+ formatAMPM(new Date) +'</p>'+
                                      '<p>'+data_get+'</p> '+
                                  '</div>'+
                              '</div>'+
                              '<audio cl controls id="source-'+ i + '" ><source  src="" type="audio/mpeg">Your browser does not support the audio element.</audio>'+
  
                      '</div>'+
                      '<div class="clearfix">&nbsp;</div>';
  
                      var robot_msg ='<div class="robot_msg">'+ 
                      '<img src="../static/images/avtar.png" class="pull-left robot-img">'+ 
                      '<div class="msj macro">'+ 
                          '<div class="text text-l">'+
                              // '<p>Cronus ' +  formatAMPM(new Date) + '</p>'+
                              '<p>'+msg+' </p> ' +
                          '</div> '+ 
                      '</div>'+ 
                      // '<a class="iconfont playpause icon-play" data-id="'+i+'" >d</a>'+
                  '</div>'+
                  '<div class="clearfix">&nbsp;</div>';
                   
                    
                      setKey("sessionId",data_get.sessionId);
                      $(".chat_msg_main").append(robot_msg);
                      $(".chat_msg_main").append(user_msg);
                      $('.chat_msg_main').animate({scrollTop: $('.chat_msg_main').prop("scrollHeight")}, 500);
                      $(".play-pause-button").hide();
  
                     /* $(".chat_msg_main").animate({
                          scrollTop: $(".chat_msg_main").scrollHeight
                      }, 300);*/
                      $("#textbox_msg").val("");
                      $('html, body').animate({
                          scrollTop: $('.text-box').offset().top
                        }, 800);
                      $('#textbox_msg').focus();
                      var text_voice = data_get; 
                      $(".send_msg").prop('value', 'Loading..');                                                                                                                     
                      // $(".send_msg").attr("disabled", true);
                      $('#source-' + i).hide();
                      if(text_voice!="") {
                          $.post("http://151.253.132.151:5000/get_audio", {text_voice: text_voice}).done(function (data) {                                                               
                              $('#source-' + i).attr('src', "http://151.253.132.151:5000/../static/generated/" + data+'.wav');
                              // $('#source-' + i).trigger("play");
                              $(".send_msg").prop('value', 'Submit');   
                              $(".send_msg").attr("disabled", false); 
                              $(".play-pause-button").show();
                               
              
                              
                          }).fail(function (jqXHR, textStatus, errorThrown) {
                              
                             // alert("Server not responding please try later.");
                                //$("audio").hide();
                                //$(".send_msg").prop('value', 'Submit'); 
                                //$(".send_msg").attr("disabled", false);
                              return false; 
                          });
                      }     
                  }).fail(function (jqXHR, textStatus, errorThrownj) {
                      $('.lds-ellipsis').hide();
                      alert("Server not responding please try later.");
                      //alert("There is an error, please try again");  commenting to prevent error popup from poping up.
                      ////location.href="index.html";
                  });;
          }
     /*     
          $.get("http://151.253.132.135:9000/cronus",
                  {

                    field: 'hi', 
                  }).done(function (data_get) {
                      i++
                      console.log(data_get);
                      $('.lds-ellipsis').hide();
                      var user_msg = ' <div class="user_msg">'+
                          '<img src="../static/images/Robobto.png" class="pull-right user-img">'+
     
                          '<div class="msj-rta macro">'+ 
                          '<a class="play-pause-button fa fa-play" data-id="'+i+'"></a>'+
  
                                  '<div class="text text-r">'+ 
                                      // '<p>User '+ formatAMPM(new Date) +'</p>'+
                                      '<p>'+data_get+'</p> '+
                                  '</div>'+
                              '</div>'+
                              '<audio cl controls id="source-'+ i + '" ><source  src="" type="audio/mpeg">Your browser does not support the audio element.</audio>'+
  
                      '</div>'+
                      '<div class="clearfix">&nbsp;</div>';

                   
                    
                      setKey("sessionId",data_get.sessionId);
                    //   $(".chat_msg_main").append(robot_msg);
                      $(".chat_msg_main").append(user_msg);
                      $('.chat_msg_main').animate({scrollTop: $('.chat_msg_main').prop("scrollHeight")}, 500);
                      $(".play-pause-button").hide();
  
                     /* $(".chat_msg_main").animate({
                          scrollTop: $(".chat_msg_main").scrollHeight
                      }, 300);*/
/*
                      $("#textbox_msg").val("");
                      $('html, body').animate({
                          scrollTop: $('.text-box').offset().top
                        }, 800);
                      $('#textbox_msg').focus();
                      var text_voice = data_get; 
                      $(".send_msg").prop('value', 'Loading..');                                                                                                                     
                      // $(".send_msg").attr("disabled", true);
                      $('#source-' + i).hide();
                      if(text_voice!="") {
                          $.post("http://151.253.132.152:5051/get_audio", {text_voice: text_voice}).done(function (data) {                                                               
                              $('#source-' + i).attr('src', "http://151.253.132.152:5051/../static/generated/" + data+'.wav');
                              // $('#source-' + i).trigger("play");
                              $(".send_msg").prop('value', 'Submit');   
                              $(".send_msg").attr("disabled", false); 
                              $(".play-pause-button").show();
                               
              
                              
                          }).fail(function (jqXHR, textStatus, errorThrown) {
                              
                             // alert("Server not responding please try later.");
                                //$("audio").hide();
                                //$(".send_msg").prop('value', 'Submit'); 
                                //$(".send_msg").attr("disabled", false);
                              return false; 
                          });
                      }     
                  }).fail(function (jqXHR, textStatus, errorThrownj) {
                      $('.lds-ellipsis').hide();
                      alert("Server not responding please try later.");
                      //alert("There is an error, please try again");  commenting to prevent error popup from poping up.
                      ////location.href="index.html";
                  });;
*/

        //   $().click(function(){
        //     // alert($(this).attr("data-id"));
        //     alert("d");
        // });

    $('#submit').on('click', function () {
        alert('ok')
        

    });

        

		$(".send_msg").click(function () {
            msg = $.trim($("#textbox_msg").val());
            $('.lds-ellipsis').show();
			if(msg!=""){
                chat(msg);
            }
            else {
                msg = 'hello there';
                chat(msg);  
            }
        })

        $('#textbox_msg').keyup(function(e){
            if(e.keyCode == 13)
            {
                $(".send_msg").trigger("click");
            }
        });


    //     audio.onended = function() {
    //       alert(audio.duration());
    //    };
        /* START MENU-JS */	

        $("body").on("click",".play-pause-button", function(){
            // alert($(this).attr('data-id'));
            if($(this).hasClass('fa-play'))
            {
                $(this).removeClass('fa-play');
                $(this).addClass('fa-pause');
                $('#source-'+$(this).attr('data-id')).trigger("play");
               
                initializeAudio($(this).attr('data-id'),$(this));


               
            }
            else
                {
                    $(this).removeClass('fa-pause');
                    $(this).addClass('fa-play');
                    $('#source-' +$(this).attr('data-id')).trigger("pause");
                    // $('#source-' +$(this).attr('data-id')).play();
                // audio.pause();
                }
        });
       
function initializeAudio(i,event)
{ 

    var x=setInterval(function(){
        var s= document.getElementById('source-'+i);
        if(s.ended){
            event.removeClass('fa-pause');
            event.addClass('fa-play');
        }
         console.log(s.ended);
    }, 300);
}
	
			$(window).scroll(function() {
			/*  if ($(this).scrollTop() > 100) {
				$('.menu-top').addClass('sticky_menu');
			  } else {
				$('.menu-top').removeClass('sticky_menu');
			  }*/
			});
			
			$(document).on('click','.navbar-collapse.in',function(e) {
			if( $(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle' ) {
				$(this).collapse('hide');
			}
			});				
		/* END MENU-JS */
        function setKey(key_name,key_value) {
            localStorage.setItem(key_name,JSON.stringify(key_value));
        }

        function getKey(key_name) {
        	if(JSON.parse(localStorage.getItem(key_name)) == null){
        		return 1;
			}else{
                return JSON.parse(localStorage.getItem(key_name));
			}

        }
		 
		
	});	
	
		/*PRELOADER JS*/
			$(window).on('load', function() {  
				$('.spinner').fadeOut();
				$('.preloader').delay(350).fadeOut('slow'); 
			}); 
        /*END PRELOADER JS*/

    var callback = function(e) {
        var username = $('#username').val();
        var password = $('#password').val();

        if (username == '' || password == '') {
            alert('please fill the fields');
        }

        else {
            $.post("http://151.253.132.135:9000/user_login", {email: username, password: password}).done(function (data) {
                
                 
                if (data.success == 'Login success') {
                    localStorage.setItem("email", username);
                    localStorage.setItem("name", data.username);
                    window.location.href= "index.html";
                }
                else {
                    alert('Not Authorize')
                }
                
            }).fail(function (jqXHR, textStatus, errorThrown) {
                
                alert("Server not responding please try later.");
                return false; 
            });
        }
        e.preventDefault();
    };
    
    $(".login-form button").keypress(function(event) {
        if (event.which == 13) callback(event);
    });


    $('#login-btn').on('click', function(event) {
        callback(event);
    });

    
		
	$('#logout').click(function() {

        $.post("http://151.253.132.135:9000/user_logout", {email: localStorage.getItem('email')}).done(function (data) {                                                               
                 
                if (data == 'Logout') {
                    localStorage.removeItem('email')
                    window.location.href = "login.html";
                }
                else {
                    alert('Not Authorize')
                }
                
            }).fail(function (jqXHR, textStatus, errorThrown) {
                
                alert("Server not responding please try later.");
                //$("audio").hide();
                //$(".send_msg").prop('value', 'Submit'); 
                //$(".send_msg").attr("disabled", false);
                return false; 
            });

        
    })
    
    $('#signup').click(function() {

        var username = $('#username').val();
        var dob = $('#dob').val();
        var city = $('#city').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var confirm_password = $('#confirm-password').val();

        if (username == '' || password == '' || city == '' || password == '' || confirm_password == '') {
            alert('please fill the fields');
        }
        else if (confirm_password !==  password) {
            alert('please type same password');
        }
        else {
            $.post("http://151.253.132.135:9000/signup", {
                username: username,
                email: email,
                password: password,
                confirm_password: confirm_password,
                dob: dob,
                city: city
            }).done(function (data) {                                                               
                 
                if (data == 'Save') {
                    alert('Save');
                    window.location.href= "login.html";
                }
                else if (data == 'Data already exist') {
                    alert('Data already exist')
                }
                else if (data == 'Email is not valid') {
                    alert('Email is not valid')
                }
                else {
                    alert('Password not matched')
                }
                
            }).fail(function (jqXHR, textStatus, errorThrown) {
                
                alert("Server not responding please try later.");
                return false; 
            });
        }
        
    })
    
        // $( "#dob" ).datepicker({
        //     changeMonth: true,
        //     changeYear: true,
        //     yearRange: "-100:+0"
        // });

})(jQuery);
