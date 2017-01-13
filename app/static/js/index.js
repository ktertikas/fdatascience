// console.log('It goes until here');
var ws = new WebSocket("ws://localhost:8888/vis");

var guidelines = 
{ 
    "Infants"       : { "VitaminC" : 30, "Fat" : 30.5, "Cholesterol" : null, "Carbohydrate" : 77.5, "Protein" : 10.05, "EnergyCal" : 593},
    "Toddlers"      : { "VitaminC" : 30, "Fat" : null, "Cholesterol" : null, "Carbohydrate" : 139.5, "Protein" : 14.5, "EnergyCal" : 1046},
    "Other children": { "VitaminC" : 30, "Fat" : 62.25, "Cholesterol" : null, "Carbohydrate" : 212.75, "Protein" : 24, "EnergyCal" : 1595},
    "Adolescents"   : { "VitaminC" : 37.5, "Fat" : 87.5, "Cholesterol" : null, "Carbohydrate" : 300, "Protein" : 45.875, "EnergyCal" : 2250},
    "Adults"        : { "VitaminC" : 40, "Fat" : 87.5, "Cholesterol" : null, "Carbohydrate" : 300, "Protein" : 50.25, "EnergyCal" : 2250},
    "Elderly"       : { "VitaminC" : 40, "Fat" : 82.5, "Cholesterol" : null, "Carbohydrate" : 283.5, "Protein" : 49.9, "EnergyCal" : 2127},
    "Very elderly"  : { "VitaminC" : 40, "Fat" : 80.5, "Cholesterol" : null, "Carbohydrate" : 275.5, "Protein" : 49.9, "EnergyCal" : 2067}
};

var nutr_arr = [];
var nutr_value = "";

ws.onopen = function(){
    // ws.send("Sent message ok");
    var e = document.getElementById("PopClass");
    document.getElementById("title").innerHTML = "Chart of Population Class " + e.options[e.selectedIndex].value;
    ws.send(e.options[e.selectedIndex].text);
};

ws.onmessage = function(event) {
    data_json = event.data;
    console.log('You\'re here');
    return_nutr();
};

function return_pop(){
	var d = document.getElementById("PopClass");
    document.getElementById("title").innerHTML = "Chart of Population Class " + d.options[d.selectedIndex].value;
    ws.send(d.options[d.selectedIndex].value);
}

function return_nutr() {
    var nutr = document.getElementById("Nutr");
    nutr_value = nutr.options[nutr.selectedIndex].value;
    var nutr_text = nutr.options[nutr.selectedIndex].text;
    var popclass = document.getElementById("PopClass").options[document.getElementById("PopClass").selectedIndex].value;

    getArray(nutr_value);

    minX = Math.min.apply(null,nutr_arr);
    maxX = Math.max.apply(null,nutr_arr);
    final_bins = findBins(nutr_arr, popclass, nutr_value);
    console.log(final_bins);
    
    var jsonBarData        = {};
    jsonBarData["key"]     = "Bins of "+popclass;
    jsonBarData["bar"]     = true;
    jsonBarData["values"]  = final_bins;
    var jsonLineData       = {};
    jsonLineData["key"]    = "Line of "+popclass;
    jsonLineData["values"] = final_bins;

    // console.log(nutr_value);

    buildBarChart(popclass, nutr_text, nutr_value, jsonBarData, jsonLineData, minX, maxX);
}

function getArray(nutr) {
    // console.log(data_json);
    nutr_arr = [];
    var json_obj = JSON.parse(data_json);
    for (var key in json_obj)
    {
       if (json_obj.hasOwnProperty(key))
       {
          nutr_arr.push(json_obj[key][nutr]);
       }
    }
    console.log(nutr)
    console.log(nutr_arr)
}

function findBins(data_arr, popclass, nutr_value){
    // data_arr  = [1704.648,1766.856,1522.408,1471.296,1694.776,1630.12,1823.36,1964.528,1964.528,1578.888,1827.792,1878.712,1933.52,1635.512,1735.848,1964.528,1361.136,1487.064,1854.368,1512.536,1772.248,1782.288,1788.016,1866.976,1571.816,1256.68,1823.36,1543.376,1806.632,2036.608];
    min_data_arr = Math.min.apply(null,data_arr);
    max_data_arr = Math.max.apply(null,data_arr);
    numbins      = 20;
    console.log("data_arr.length: "+data_arr.length);
    console.log("min: "+min_data_arr);
    console.log("max: "+max_data_arr);

    var bins = d3.layout.histogram()    // create layout object
    .bins(numbins)   // to use 20 bins
    .range([min_data_arr, max_data_arr])    // to cover range from 0 to 1
    (data_arr); // group the data into the bins
    // bins[i] is an array of values in the ith bin
    // bins[i].x is the lower bounds of the ith bin
    // bins[i].dx is the width of the ith bin
    // bins[i].x + bins[i].dx is the upper bounds of the ith bin
    // bins[i].y is the number of values in the ith bin
    // for (i = 0; i < bins.length; i++) {
    //     console.log(bins[i]);
    // }

    var gd_value = guidelines[popclass][nutr_value];
    var min_bin = bins[0].x;
    var max_bin = bins[bins.length-1].x;
    var gap = (max_bin-min_bin)*0.1;
    var minX = Math.floor(min_bin-gap);
    var maxX = Math.floor(gd_value+gap);
    if(minX <= 0) { minX = 0; }
    if((gd_value > min_bin && gd_value < max_bin) || gd_value == null) { maxX = Math.floor(max_bin+gap); }
    var final_bins = new Array(bins.length+2);
    final_bins[0]    = new Array(2);
    final_bins[0][0] = minX;
    final_bins[0][1] = NaN;
    for (var i = 0; i < bins.length; i++) {
        final_bins[i+1]    = new Array(2);
        final_bins[i+1][0] = bins[i].x;
        final_bins[i+1][1] = bins[i].y;
    }
    final_bins[final_bins.length-1]    = new Array(2);
    final_bins[final_bins.length-1][0] = maxX
    final_bins[final_bins.length-1][1] = NaN;

    return final_bins;
}

function buildBarChart(popclass, nutr_text, nutr_value, jsonBarData, jsonLineData, minX, maxX){
    // d3.selectAll("svg > *").remove();
    d3.selectAll("svg").remove();
    d3.select("#chart1").append("svg");
    var svg = d3.select("#chart1 svg");
    var height = parseInt(svg.style("height"), 10);
    var width = parseInt(svg.style("width"), 10);

    // var xaxis = "Nums of "+popclass;
    var yaxis = "Number of "+popclass;
    var testdata = [jsonBarData, jsonLineData]
        .map(function(series) {
            series.values = series.values.map(function(d) { return {x: d[0], y: d[1] } });
            return series;
        });
    var chart;
    nv.addGraph(function() {
        chart = nv.models.linePlusBarChart()
            .margin({top: 50, right: 80, bottom: 30, left: 80})
            .legendLeftAxisHint('')
            .legendRightAxisHint('')
            .color(d3.scale.category10().range())
            .focusEnable(false)
            .interpolate('basis');
        chart.xAxis.axisLabel(nutr_text).axisLabelDistance(-10);
        chart.y1Axis.axisLabel(yaxis);
        chart.y2Axis.axisLabel(yaxis);
        chart.xAxis.tickFormat(function(d) { return d3.format(',f')(d) });

        // console.log("maxX: "+maxX);
        // maxXX = Math.floor((maxX+100)/100)*100;
        // console.log("maxXX: "+maxXX);
        // chart.lines.forceX([minX, maxX]).padData(false);
        // chart.bars.forceX([minX, maxX]).padData(false);

        chart.lines.forceY([0]).padData(false);
        chart.bars.forceY([0]).padData(false);

        d3.select('#chart1 svg')
            .datum(testdata)
            .transition().duration(500).call(chart);

        nv.utils.windowResize(function(){
            chart.update();
        });
        // chart.dispatch.on('stateChange', function(e) { nv.log('New State:', JSON.stringify(e)); });

        // d3.selectAll('.nv-bar').attr('width','15px');
        // addTitle();
        drawGuideLine();
        // window.addEventListener('resize', addTitle);
        window.addEventListener('resize', drawGuideLine);

        //ADD TITLE in SVG
        function addTitle(){
            d3.selectAll("#svgtitle").remove();
            var height = parseInt(svg.style("height"), 10);
            var width = parseInt(svg.style("width"), 10);
            var x = (width / 2);
            var y = 12;
            var ctext = "Chart of "+popclass;
            d3.select('#chart1 svg')
                .append("text")
                .attr("id","svgtitle")
                .attr("x", x)          
                .attr("y", y)
                .attr("text-anchor", "middle")  
                .style("font-size", "16px") 
                .style("text-decoration", "underline")
                .text(ctext);
        }

        //CREATE GUIDELINES LINE
        function drawGuideLine(){
            d3.selectAll("#svgline").remove();
            d3.selectAll("#svgtext").remove();
            d3.selectAll("#svgtext2").remove();
            var gd_value = guidelines[popclass][nutr_value];
            if(guidelines[popclass][nutr_value] !== null) {
                // console.log("gd_value: "+gd_value);
                var margin = {top: 50, right: 80, bottom: 30, left: 80}; //margin from chart declaration
                var xScale = chart.xAxis.scale(); //calculate the yScale
                var xValue = gd_value;
                var gd_color = "red";
                svg.append("line")
                    .attr("id","svgline")
                    .style("stroke", gd_color)
                    .style("stroke-width", "1px")
                    .attr("x1", xScale(xValue) + margin.left)
                    .attr("y1", margin.top)
                    .attr("x2", xScale(xValue) + margin.left)
                    .attr("y2", height - margin.bottom);
                
                var gltext = "Guideline";
                var gltext_value = gd_value;
                if(nutr_value=="VitaminC"||nutr_value=="Cholesterol"){
                    gltext_value = gltext_value + " (mg)";
                }else if(nutr_value=="Fat"||nutr_value=="Carbohydrate"||nutr_value=="Protein"){
                    gltext_value = gltext_value + " (g)";
                }else if(nutr_value=="EnergyCal"){
                    gltext_value = gltext_value + " (Cal)";
                }

                var text_size = "12px";
                d3.select("#chart1 svg")
                    .append("text")
                    .attr("id","svgtext")
                    .style("fill", gd_color)
                    .style("font-size", text_size)
                    .attr("x", xScale(xValue) + margin.left)
                    .attr("y", margin.top-16)
                    .attr("text-anchor", "middle")
                    .text(gltext);

                d3.select("#chart1 svg")
                    .append("text")
                    .attr("id","svgtext2")
                    .style("fill", gd_color)
                    .style("font-size", text_size)
                    .attr("x", xScale(xValue) + margin.left)
                    .attr("y", margin.top-3)
                    .attr("text-anchor", "middle")
                    .text(gltext_value);
            }
        }

        return chart;
    });
}