$(document).ready(function() {


	// Adding current date
	// function GetMonthName(monthNumber) {
	//   var months = ['January', 'February', 'March', 'April', 'May', 'June',
	//   'July', 'August', 'September', 'October', 'November', 'December'];
	//   return months[monthNumber-1];
	// }
	var d = new Date();
	var strDate =  + (d.getMonth()+1) + ", " + d.getFullYear();

	$('.date').text(strDate);


	// creates
	$("input").focus(function() {
		// sets variable of name of selected input
		var focusedName = $(this).attr("name");

		// takes the input via keyups and creates a classname for it to go to  
		$(this)
		  .keyup(function() {
		    var value = $(this).val();
		    console.log(focusedName);
		    $( "." + focusedName ).text( value );
		  });

	});

	$(function(){
	  $.datepicker.setDefaults(
	    $.extend( $.datepicker.regional[ '' ] )
	  );
	  $( '#eventDate, #consultDate' ).datepicker();
	});

	function formSubmit() {

		$('#formSubmit').click(function() {
			var firstName = $('#firstname').val();
			var lastName = $('#lastname').val();
			var eventDate = $('.event-date').val();
			var consDate = $('.consultation-date').val();

			$('.subscriber').text(firstName + " " + lastName);
			$('.event').text("on " + eventDate);
			$('.consultation').text(" on " + consDate);
			// $('.subscriber').text(phone);
			// $('.subscriber').text(firstName);
			$('.container').addClass('hide');
			$('.mailTemplate').removeClass('hide');
			
		});

	}


formSubmit();



});