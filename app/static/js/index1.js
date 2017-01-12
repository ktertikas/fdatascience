// console.log('It goes until here');
var ws = new WebSocket("ws://localhost:8888/vis2");

var nutr_arr   = [];
var nutr_value = "";
var nutr_text  = "";

ws.onopen = function(){
    // ws.send("Sent message ok");
    console.log("ws.onopen");
    var e = document.getElementById("Nutr");
    nutr_value = e.options[e.selectedIndex].value;
    nutr_text = e.options[e.selectedIndex].text;
    ws.send(nutr_value);
};

ws.onmessage = function(event) {
    console.log("ws.onmessage");
    data_json = event.data;
    console.log(data_json);
    do_nutr();
};

function return_nutr() {
	var d = document.getElementById("Nutr");
    nutr_value = d.options[d.selectedIndex].value;
    nutr_text = d.options[d.selectedIndex].text;
    ws.send(nutr_value);
}

function do_nutr() {
    console.log("do_nutr");
    var json_obj = JSON.parse(data_json);
    console.log(json_obj);
    buildBarChart(json_obj);
}

function buildBarChart(json_obj){
    d3.selectAll("svg > *").remove();

    barChart = [
        {
            key: "XXX",
            values: json_obj
        }
    ];
    console.log(barChart);
    
    nv.addGraph(function() {
        var chart = nv.models.discreteBarChart()
            .x(function(d) { return d.label })
            .y(function(d) { return d.value })
            .staggerLabels(true)
            .staggerLabels(barChart[0].values.length > 10)
            .showValues(true)
            .duration(250)
            ;
        chart.xAxis.axisLabel("Population Class");
        chart.yAxis.axisLabel(nutr_text);
        chart.yAxis.tickFormat(d3.format(',f'));
        chart.valueFormat(d3.format(',f'));

        d3.select('#chart1 svg')
            .datum(barChart)
            .call(chart);
        nv.utils.windowResize(chart.update);
        return chart;
    });
}