
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
        node_target1.empty()
    } 
    function displayDates(node,node_target1) {
        var title = node.val();
        var id = act_id[title] 
        console.log(id)
            node_target1.empty()
                for (activity in act_dates) {
                    if (act_id[activity]===id){
                        var limit = act_dates[activity].length;
                        for (let i = 0; i < limit; i++) {
                            var date_string = act_dates[activity][i];
                            var date = new Date(date_string);
                            date = formatDate(date);
                            var date = $("<option>").append(date);
                            node_target1.append(date);
                        };
                    } ;
                    
 
                }; 

    };
    //function from stack overflow https://stackoverflow.com/questions/23593052/format-javascript-date-as-yyyy-mm-dd
    function formatDate(date) {
        var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();
    
        if (month.length < 2) 
            month = '0' + month;
        if (day.length < 2) 
            day = '0' + day;
    
        return [year, month, day].join('/');
    }

    console.log(act_dates)
    
    var node_source = $("#activity_title_booked");
    var node_target1 =  $("#date_chosen");
    node_source.change(function(){
        displayDates(node_source,node_target1)
    })
      
        
    
            
    
     
});
