var n = 10,
    oxymeter_duration = 1000,
    now = new Date(Date.now() - oxymeter_duration); //is set to 0.75 seconds behind now;

var countTotal = 1;
var oxymeterCount = 0;
var oxymeterData = d3.range(n).map(function() { return 0; }); // Create an empty data set e.g. 0,0,0,0, etc

var oxymeter_margin = {top: 6, right: 0, bottom: 20, left: 50},
    oxymeter_width = 100 - oxymeter_margin.right,
    oxymeter_height = 50 - oxymeter_margin.top - oxymeter_margin.bottom;

// X axis
var oxymeter_x = d3.time.scale()
    .domain([now - (n - 2) * oxymeter_duration, now - oxymeter_duration])  // current time - .75 s  - (486) * 750, current time
    .range([0, oxymeter_width]);

// Y axis
var oxymeter_y = d3.scale.linear()
    .range([oxymeter_height, 0]);

var oxymeter_line = d3.svg.line()
    .interpolate("basis")
    .x(function(d, i) { return oxymeter_x(now - (n - 1 - i) * oxymeter_duration); })
    .y(function(d, i) { return oxymeter_y(d); });

var oxymeter_svg = d3.select("#oxygraph").append("p").append("svg")
    .attr("width", oxymeter_width + oxymeter_margin.left + oxymeter_margin.right)
    .attr("height", oxymeter_height + oxymeter_margin.top + oxymeter_margin.bottom)
    .style("margin-left", -oxymeter_margin.left + "px")
  .append("g")
    .attr("transform", "translate(" + oxymeter_margin.left + "," + oxymeter_margin.top + ")");

oxymeter_svg.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", oxymeter_width)
    .attr("height", oxymeter_height);

// X Axis
var oxymeter_axis = oxymeter_svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + oxymeter_height + ")")
    .call(oxymeter_x.axis = d3.svg.axis().scale(oxymeter_x).orient("bottom"));

// Y Axis
var oxymeter_yaxsis = oxymeter_svg.append("g")
  .attr("class", "y axis")
  .call(d3.svg.axis().scale(oxymeter_y).ticks(3).orient("left"));
    
// Line
var oxymeter_path = oxymeter_svg.append("g")
    .attr("clip-path", "url(#clip)")
  .append("path")
    .data([oxymeterData])
    .attr("class", "line");
  
// Y axis label
// yaxsis.append("text")
//     .attr("transform", "rotate(-90),translate(-250,-40)")
//     .text("Interactions Per Second");

var oxymeter_tick = function () {

    // update the domains
    now = new Date();
    
    // your data minimum and maximum e.g. domain([0, 20]) 
    //  now - 0.75 seconds - (245) * 750
    oxymeter_x.domain([now - (n - 2) * oxymeter_duration, now - oxymeter_duration]);
    
    // console.log(oxymeterData);

    oxymeter_y.domain([0, d3.max(oxymeterData)]);

    // push the accumulated count onto the back, and reset the count
    oxymeterData.push(Math.min(100, oxymeterCount));
 
    oxymeterCount = 0;

    // redraw the line
    oxymeter_svg.select(".line")
        .attr("d", oxymeter_line)
        .attr("transform", null);

    // slide the x-axis left
    oxymeter_axis.transition()
        .duration(oxymeter_duration)
        .ease("linear")
        .call(oxymeter_x.axis);

    // slide the line left
    oxymeter_path.transition()
        .duration(oxymeter_duration)
        .ease("linear")
        .attr("transform", "translate(" + oxymeter_x(now - (n - 1) * oxymeter_duration) + ")")
        .each("end", oxymeter_tick);

    // Y Axis
    oxymeter_yaxsis.transition()
        .attr("class", "y axis")
        .ease("linear")
        .call(d3.svg.axis().scale(oxymeter_y).ticks(2).orient("left"));

    // pop the old data point off the front
    oxymeterData.shift();

}

oxymeter_tick();
