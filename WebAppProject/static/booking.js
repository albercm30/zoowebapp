
$(window).on("load", function() {
    /*
    function myFunc(vars) {
        console.log(vars);
        return vars
    };
    myFunc(act_dates);
    */
    //var act_booked = $("#act_booked");

    function displayDates(node,node_target,reference_id,id) {
        node.click(function(){
                for (activity in act_dates) {
                    if (act_id[activity]===reference_id){
                        var limit = act_dates[activity].length;
                        for (let i = 0; i < limit; i++) {
                            var option = $("<option>").html(act_dates[activity][i] );
                            node_target.append(option);
                        };
                    } ;
                    
 
                };       
        });
    };



    for (act in act_dates) {
        var id = act_id[act];
        var reference_id = act_id[act];
        var node_source = $("#r" + reference_id);
        var node_target =  $("#d" + reference_id);
        displayDates(node_source,node_target,reference_id,id)
        

        
    } 
            
    
     
});
