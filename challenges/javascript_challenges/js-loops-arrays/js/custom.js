$(document).ready(function(){



var myList = ['Eggs', 'Bread', 'Milk', 'Kombucha', 'Cheese', 'ICE CREAM!!!', 'Toothpaste'];

for (var i = 0; i < myList.length; i++) {
	$('ul').append('<li class="active" href="#">' + myList[i] + '</li>');
}

$('li').hover(function(){
	$(this).css('box-shadow', '1px 1px 2px #000');
}, function() {
	$(this).css('box-shadow', 'none')
	}
);

$('li').click(function() {
	if ($('li').hasClass('active')) {
		// $(this).fadeOut(1000).fadeIn(1000);
		$(this).removeClass('active').addClass('un-active ');
	}
});




});