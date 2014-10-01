$(document).ready(function(){


    /* websockets */

    namespace = ''; // change to an empty string to use the global namespace

    var url ='http://' + document.domain + ':' + location.port + namespace;

    var socket = io.connect(url);

    socket.on('connect', function() {
        console.log("socket connected");
        socket.emit('eeg_start', function(data) {
            console.log(data);
        });
    });

    

    var seriesData;
    var palette = new Rickshaw.Color.Palette( { scheme: 'classic9' } );

    // draw bar chart
    Rickshaw.Graph.Socketio.Static = Rickshaw.Class.create( Rickshaw.Graph.Socketio, {
            request: function() {
              var socket = io.connect(this.dataURL);
              thisData = this;
                socket.on('brain', function (data) {
                    // console.log(data);
                   thisData.success(data);
                });
            }
        } );

    var EEGGraph = new Rickshaw.Graph.Socketio.Static( {
        element: document.getElementById("eeg"),
        width: window.innerWidth,
        height: 400,
        renderer: 'line',
        dataURL: url,
        onData: function(d) { 
                var seriesData=d.series;
                var series = [
                    {
                        color: palette.color(),
                        data: seriesData[0].data,
                        name: seriesData[0].name
                    }, {
                        color: palette.color(),
                        data: seriesData[1].data,
                        name: seriesData[1].name
                    }, {
                        color: palette.color(),
                        data: seriesData[2].data,
                        name: seriesData[2].name
                    }, {
                        color: palette.color(),
                        data: seriesData[3].data,
                        name: seriesData[3].name
                    }, {
                        color: palette.color(),
                        data: seriesData[4].data,
                        name: seriesData[4].name
                    }, {
                        color: palette.color(),
                        data: seriesData[5].data,
                        name: seriesData[5].name
                    }, {
                        color: palette.color(),
                        data: seriesData[6].data,
                        name: seriesData[6].name
                    }, {
                        color: palette.color(),
                        data: seriesData[7].data,
                        name: seriesData[7].name
                    }
                ]
                return series;
            }
    } );


    var isDraw=false;
    var svg,x,y,width,height,margin;

    socket.on('brain', function(data) {
        console.log(data);
        var brainValues=[
            {
                "name": "attention",
                "value": data.point.attention // Math.random()*200//
            },
            {
                "name" : "meditation",
                "value": data.point.meditation // Math.random()*200// 
            }
        ];

        // console.log(brainValues);
        if(!isDraw){
            margin = {top: 20, right: 20, bottom: 30, left: 40};
            width = window.innerWidth - margin.left - margin.right;
            height = 400 - margin.top - margin.bottom;

            x = d3.scale.ordinal()
                .rangeRoundBands([0, width], .1);

            y = d3.scale.linear()
                .range([height, 0]);

            var xAxis = d3.svg.axis()
                .scale(x)
                .orient("bottom");

            var yAxis = d3.svg.axis()
                .scale(y)
                .orient("left");
                // .ticks(10, "%");

            svg = d3.select("#brain-values").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
              .append("g")
                .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            x.domain(brainValues.map(function(d) { return d.name; }));
            y.domain([0, 200]);

            svg.append("g")
              .attr("class", "x axis")
              .attr("transform", "translate(0," + height + ")")
              .call(xAxis);

            svg.append("g")
              .attr("class", "y axis")
              .call(yAxis)
            .append("text")
              .attr("transform", "rotate(-90)")
              .attr("y", 6)
              .attr("dy", ".71em")
              .style("text-anchor", "end")
              .text("Value");
         
            svg.selectAll(".bar")
              .data(brainValues)
            .enter().append("rect")
              .attr("class", "bar")
              .attr("x", function(d) { return x(d.value); })
              .attr("width", x.rangeBand())
              .attr("y", function(d) { return y(d.value); })
              .attr("height", function(d) { return height - y(d.value); });

            isDraw=true;
        } else {
             update(brainValues);
        }

        function update (_data) {
            svg.selectAll(".bar")
              .data(_data)
              .transition()
              .attr("x", function(d) { return x(d.name); })
              .attr("width", x.rangeBand())
              .attr("y", function(d) { return y(d.value); })
              .attr("height", function(d) { return height - y(d.value); });
        }
    });







    /* GUI DAT */
    // var gui = new dat.GUI();
    // gui.add(EEGGraph, 'message');
    // gui.add(EEGGraph, 'speed', -5, 5);
    // gui.add(EEGGraph, 'displayOutline');
    // gui.add(EEGGraph, 'explode');


    /*
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    */
});
