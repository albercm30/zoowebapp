
$(window).on("load", function() {
    /*
    function myFunc(vars) {
        console.log(vars);
        return vars
    };
    myFunc(act_dates);
    */
    var act_booked = $("#act_booked").html();
    console.log(act_booked);
    for (act in act_dates) {
        console.log(act);
        if (act === act_booked){
            var option = $("<option>").html(act_dates[act]);
            $("#date_chosen").append(option);
        } 
        
    } 
});
