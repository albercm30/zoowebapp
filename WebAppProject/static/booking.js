
$(window).on("load", function() {
    /*
    function myFunc(vars) {
        console.log(vars);
        return vars
    };
    myFunc(act_dates);
    */
    //var act_booked = $("#act_booked");

    function other_nodes(id) {
        var other_n =[];
        for (act in act_dates) {
            if (act_id[act]!==id){
                other_n.push(act_id[act]);
            } 
        } 
        return other_n;
    } 

    function deleteDates(id) {
        var other_n = other_nodes(id);
        for (n in other_n) {
            $("#date" + other_n[n]).empty()
        } 
    } 
    function displayDates(node,node_target1,id) {
        node.click(function(){
            node_target1.empty()
                for (activity in act_dates) {
                    if (act_id[activity]===id){
                        var limit = act_dates[activity].length;
                        for (let i = 0; i < limit; i++) {
                            var date = $("<option>").html(act_dates[activity][i] );
                            node_target1.append(date);
                        };
                    } ;
                    
 
                }; 
            deleteDates(id);   
        });

    };


    for (act in act_dates) {
        var id = act_id[act];
        var node_source = $("#r" + id);
        var node_target1 =  $("#date" + id);
        displayDates(node_source,node_target1,id)  
        
    } 
            
    
     
});
