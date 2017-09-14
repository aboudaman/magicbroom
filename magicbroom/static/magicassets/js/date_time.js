// Date and Time set up
$(document).ready(function() {
  // $( "#id_Date" ).datepicker();
  $('#id_booking_time').pickatime({
    min: [6,30],
    max: [19,0]
  });

  $('#id_booking_date').pickadate({
    format: 'mm/dd/yyyy',
    min: 'picker__day--today',
    max: new Date(2050,1,30)
  });

});
