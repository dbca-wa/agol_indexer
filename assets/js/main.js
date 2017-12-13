$(document).ready(function() {

	$('#cal').calendar({
		today: true,
		initialDate: null,
		monthFirst: false,
		 ampm: false,
		formatter: {
			date: function (date, settings) {
				if (!date) return '';
				var day = date.getDate();
				var month = date.getMonth() + 1;
				var year = date.getFullYear();
				return day + '/' + month + '/' + year;
			}
		}
	});

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

	if (window.location.href.includes('search') || window.location.href.includes('dependencies')) {
		console.log('find')
		$('.ui.card').each(function(index) {
			console.log(index)
			$(this).find('.card-accordion').removeClass('accordion')
		})
	}

	$('.ui.accordion').accordion();

	$('.activating.element').popup();

	$('.link-list').each(function(i, val) {
		if($(this).find('li').length == 0) {
			$(this).remove()
		}
	})

	$('.card-accordion').click(function() {
		if ($(this).find('i').hasClass('down')) {
			$(this).find('i').addClass('up')
			$(this).find('i').removeClass('down')
			$(this).find('.accord-exp-min').text('minimise')
		} else {
			$(this).find('i').addClass('down')
			$(this).find('i').removeClass('up')
			$(this).find('.accord-exp-min').text('expand')
		}
	})
})