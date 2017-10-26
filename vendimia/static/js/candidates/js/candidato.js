$(function(){
	 $('#id_fecha_nacimiento').fdatepicker({
		initialDate: '02-12-1989',
		format: 'mm/dd/yyyy',
		disableDblClickSelection: true,
		closeButton: true
	});
	 var nowTemp = new Date("1900-03-25");;
	var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
	var checkin = $('#id_escuela_inicio').fdatepicker({
		onRender: function (date) {
			return date.valueOf() < now.valueOf() ? 'disabled' : '';
		}
	}).on('changeDate', function (ev) {
		if (ev.date.valueOf() > checkout.date.valueOf()) {
			var newDate = new Date(ev.date)
			newDate.setDate(newDate.getDate() + 1);
			checkout.update(newDate);
		}
		checkin.hide();
		$('#id_escuela_fin')[0].focus();
	}).data('datepicker');
	var checkout = $('#id_escuela_fin').fdatepicker({
		onRender: function (date) {
			return date.valueOf() <= checkin.date.valueOf() ? 'disabled' : '';
		}
	}).on('changeDate', function (ev) {
		checkout.hide();
	}).data('datepicker');


});

