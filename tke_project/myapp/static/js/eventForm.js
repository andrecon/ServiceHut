$(function(){
    var dateObj = new Date();
    var month = dateObj.getUTCMonth() + 1; //months from 1-12
    var day = dateObj.getUTCDate();
    var year = dateObj.getUTCFullYear();

    //newdate = month + "-" + day + "-" + year;
    newdate = year + "-" + month + "-" + day;

    var $j = jQuery.noConflict();
	$j('#id_created_date').fdatepicker({
        initialDate: newdate,
        //format: 'mm-dd-yyyy',
        format: 'yyyy-mm-dd',
		disableDblClickSelection: true,
		leftArrow:'<<',
		rightArrow:'>>',
		closeIcon:'X',
		closeButton: true
    });
});