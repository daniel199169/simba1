(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();
	var startCalendars = function () {
		$('#bc_signature_date').datepicker({todayHighlight: true});
		$('#swms_date').datepicker({todayHighlight: true});
		$('#so_signature_date_1').datepicker({todayHighlight: true});
		$('#so_signature_date_2').datepicker({todayHighlight: true});
		$('#so_signature_date_3').datepicker({todayHighlight: true});
		$('#so_signature_date_4').datepicker({todayHighlight: true});
		$('#so_signature_date_5').datepicker({todayHighlight: true});
		$('#so_signature_date_6').datepicker({todayHighlight: true});
		$('#so_signature_date_7').datepicker({todayHighlight: true});
		$('#so_signature_date_8').datepicker({todayHighlight: true});
		$('#so_signature_date_9').datepicker({todayHighlight: true});
		$('#so_signature_date_10').datepicker({todayHighlight: true});
	};
	startCalendars();
})(jQuery);
