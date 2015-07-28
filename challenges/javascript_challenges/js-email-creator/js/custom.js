$(document).ready(function() {

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

	function formSubmit() {

		$('#formSubmit').click(function() {
			var firstName = $('#firstname').val();
			var lastName = $('#lastname').val();
			var phone = $('#email').val();
		});

	}

formSubmit();




});