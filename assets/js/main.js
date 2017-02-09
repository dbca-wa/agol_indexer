$(document).ready(function() {
	
	$('.ui.dropdown').dropdown()

	$('.ui.dropdown.search-dropdown').dropdown({
		fullTextSearch: true,
		allowAdditions: true,
		hideAdditions: false,
		message: {
			addResult: 'Search <b>{term}</b>'
		}
	})

	$('.ui.accordion').accordion();

	$('.activating.element').popup();

	$('.link-list').each(function(i, val) {
		if($(this).find('li').length == 0) {
			$(this).remove()
		}
	})
})