$(document).ready(function() {
	
	$('.ui.dropdown').dropdown({
		fullTextSearch: true,
		allowAdditions: true,
		hideAdditions: false,
		message: {
			addResult: 'Search <b>{term}</b>'
		}
	})

	$('.ui.accordion').accordion();

	$('.activating.element').popup();
})