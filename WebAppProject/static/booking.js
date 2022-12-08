
$(window).on("load", function() {
    /*
    function myFunc(vars) {
        console.log(vars);
        return vars
    };
    myFunc(act_dates);
    */
    //var act_booked = $("#act_booked");

    
        
    for (act in act_dates) {
        var reference_id = act_id[act];
        var node = $("#" + reference_id);
        node.prop("checked", true);
        
        if (node.is(':checked')){
            console.log(node);
            for (activity in act_dates) {
                var option = $("<option>").html(act_dates[activity]);
                $("#date_chosen").append(option);
            } 
            
            
        } 
        
    } 
            
    
     
});
