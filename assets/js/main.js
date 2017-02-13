$(document).ready(function() {
	
	$('.ui.dropdown').dropdown({
		fullTextSearch: true
	})

	$('.ui.dropdown.search-dropdown').dropdown({
		fullTextSearch: true,
		allowAdditions: true,
		hideAdditions: false,
		message: {
			addResult: 'Search <b>{term}</b>'
		},
		onChange: function(value, text, $selectedItem) {
			if (value) {
				$('.viewer-button').removeClass('disabled')
			}
		}
	})

	$('.ui.dropdown.join-item-dropdown').dropdown({
		fullTextSearch: true,
		onChange: function(value, text, $selectedItem) {
			if (value) {
				$('.join-select-button').removeClass('disabled')
			}
		}
	})

	$('.ui.dropdown.add-list').dropdown({
		fullTextSearch: true,
		onChange: function(value, text, $selectedItem) {
			if (value) {
				$(this).parent().parent().find('.join-add-button').removeClass('disabled')
			}
		}
	})

	$('.ui.accordion').accordion();

	$('.activating.element').popup();

	$('.link-list').each(function(i, val) {
		if($(this).find('li').length == 0) {
			$(this).remove()
		}
	})

	$('.create-name').keyup(function() {
		if ($(this).val() == "" || $('.create-description').val() == "" ) {
			$('.add-join-button').addClass('disabled')
		} else {
			$('.add-join-button').removeClass('disabled')
		}
	})

	$('.create-description').keyup(function() {
		if ($(this).val() == "" || $('.create-name').val() == "" ) {
			$('.add-join-button').addClass('disabled')
		} else {
			$('.add-join-button').removeClass('disabled')
		}
	})
	
})