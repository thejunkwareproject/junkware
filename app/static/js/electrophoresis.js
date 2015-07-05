var measures=[130, 560, 2020, 2320, 4360, 6560, 9420, 23130,1500, 1302];

var DNAViewer =  function(_DNA_seq, _divName,_width,_height){
    var margin = {top: 40, right: 10, bottom: 30, left: 10};
    this.DNA_seq = _DNA_seq;
    this.divName = _divName;
    this.margin = margin;
    this.width = _width - margin.left - margin.right;
    this.height = _height - margin.top - margin.bottom;
    this.enzymes = [
        {"class":"0","sequence":"CCWGG", "name" : "EcoRII"},
        {"class":"1","sequence":"GGATCC", "name" : "BamHI"},
        {"class":"1","sequence":"AAGCTT", "name" : "HindIII"},
        {"class":"1","sequence":"TCGA", "name" : "TaqI"},
        {"class":"2","sequence":"GCGGCCGC", "name" : "NotI"},
        {"class":"1","sequence":"GANTCA", "name" : "HinfI"},
        {"class":"0","sequence":"GATC", "name" : "Sau3A"},
        {"class":"3","sequence":"CAGCTG", "name" : "PvuII"},
        {"class":"3","sequence":"CCCGGG", "name" : "SmaI"},
        {"class":"2","sequence":"GGCC", "name" : "HaeIII"},
        {"class":"2","sequence":"GACGC", "name" : "HgaI"},
        {"class":"2","sequence":"AGCT", "name" : "AluI"},
        {"class":"3","sequence":"GATATC", "name" : "EcoRV"},
        {"class":"5","sequence":"GGTACC", "name" : "KpnI"},
        {"class":"5","sequence":"CTGCAG", "name" : "PstI"},
        {"class":"5","sequence":"GAGCTC", "name" : "SacI"},
        {"class":"1","sequence":"GTCGAC", "name" : "SalI"},
        {"class":"3","sequence":"AGTACT", "name" : "ScaI"},
        {"class":"1","sequence":"ACTAGT", "name" : "SpeI"},
        {"class":"5","sequence":"GCATGC", "name" : "SphI"},
        {"class":"3","sequence":"AGGCCT", "name" : "StuI"},
        {"class":"1","sequence":"TCTAGA", "name" : "XbaI"}
    ];
    return this;
}

DNAViewer.prototype.createSvg = function () {
    console.log("DNA : create SVG");
    // console.log(this);
    //canvas
    var margin = this.margin
        width = this.width,
        height = this.height;

    var svg = d3.select(this.divName).append("svg")
        .attr("id","s")
        .attr("width", this.width + margin.left + margin.right)
        .attr("height", this.height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
    // tooltips : show and hide tooltips through mousehover
    $(this.divName +" svg").on("mouseover",this,function(){
        $(".tooltip").show();
    });

    $(this.divName+ " svg").on("mouseout",this,function(){
        $(".tooltip").hide();
    });
}

DNAViewer.prototype.cutSequences = function(){
    var len_seq_container_proto = [];

    var DNA_seq = this.DNA_seq;

    var enzymes = this.enzymes;
    //make a masure container
    len_seq_container_proto[0] =  measures;

    //assign selected cuttted secuence.
    (function(){
        var where_to_cut = null;
        var cuttings;

        $(enzymes).each(function(index,element){
            // console.log(element);
            
            cuttings = enzymes[index].sequence.toUpperCase();
            // console.log(cuttings);

            where_to_cut=enzymes[index].class.toUpperCase();
            // console.log(where_to_cut);

            // split DNA sequence
            (function(){
                var len_seq = [];
             

                var splitted = DNA_seq.split(cuttings);
                
                // console.log(DNA_seq,splitted);
                for (var i=0; i < splitted.length; i++){
                    splitted[i] = splitted[i].replace(/\s*/g, "");
                    len_seq[i] = splitted[i].length;
                
                    //distribute vanished sequence by split.
                    if(where_to_cut){
                        var left = parseInt(where_to_cut);
                        var right = cuttings.length - parseInt(where_to_cut);
                        if(len_seq.length == 1){
                            len_seq[0] += left+right;
                        } else{
                            for(var j=0; j<len_seq.length-1;j++){
                                len_seq[j] += left;
                            }
                            for(j=1; j<len_seq.length;j++){
                                len_seq[j] += right;
                            }
                        }
                    }
                }
                len_seq_container_proto[index+1] =  len_seq;
            })();
        });
    })();
    
    // console.log(len_seq_container_proto);
    this.len_seq_container = len_seq_container_proto;
    return len_seq_container_proto;
};

DNAViewer.prototype.display = function() {

    // console.log("display Gel");

    var enzymes = this.enzymes;
    var color = d3.scale.category20b();
    var svg = d3.select(this.divName + " svg")

    // console.log(svg);
    var width = this.width,
        height = this.height,
        margin = this.margin
        len_seq_container = this.len_seq_container;

    //rectのエフェクト
    var rectEff = svg.append("defs")
        .append("filter").attr("id", "bands").attr("height","500%").attr("widht","100%")
        .append("feGaussianBlur").attr("in", "SourceGraphic").attr("stdDeviation", 2).attr("result", "blur")
        .append("feOffset").attr("result","offsetBlur").attr("dx",0).attr("dy",-5)
        .append("feBrend").attr("in","blur").attr("in2","offsetBlur").attr("mode","normal");

    //make max value
        var marged_list = d3.merge(len_seq_container);
        var max_value = d3.max(marged_list);


    var yScale = d3.scale.sqrt() 
        .domain([0, max_value]).range([height,0]);

    //ウェルを移動しながら作成
    var wells = svg.selectAll("g .well")
        .data(len_seq_container).enter()
        .append("g")
        .attr("class", "well")
        .attr("transform", function(d,i){
            return "translate(" + i*(width/enzymes.length) + "," + 0 + ")";
        });

    var upper_tooltips = wells.append("text")
        // .attr("class","tooltip")
        .attr("fill","white")
        .attr("font-size","11px")
        .attr("x",0)
        .attr("y",-(margin.top - 9))
        .text(function(d,i){
             // console.log(i,enzymes[i]);
            if(enzymes[i] != undefined) return enzymes[i].name;
            else return
        });

    //rect作成
    var rects = wells.selectAll("g .vertical_band") 
        .data(function(d){return d;})
        .enter()
        .append("g")
        .attr("class","vertical_band");

    //rect属性
    var rectAttr = rects
        .append("rect")
        .attr("x", function(d){return 2;})
        .attr("y", function(d){return 0;})//各dを最大値とwidthにスケールを合わせた。
        .attr("width", 38)
        .attr("height", 12)
        .attr("fill",function(i){return  color(Math.floor((Math.random()*i)+1)) })
        .attr("filter", "url(#bands)")

        .transition()
            .duration(27000)
            .delay(function(d, i){
                return i * 750
            })
            .attr("height",function(d){ return 1+((height-yScale(d))/60);})
            .attr("y",function(d){ return yScale(d);});
            

    var each_tooltips = rects.append("text")
                        .attr("class","tooltip")
                        .attr("fill","white")
                        .attr("font-size","5px")
                        .attr("x",0)
                        .attr("y",function(d){ return yScale(d);})
                        .text(function(d){return d;});
                    
    $(".tooltip").hide();
};

DNAViewer.prototype.resetDisplay = function() {
    d3.select(this.divName + " .well").remove();
    d3.selectAll(this.divName + " .well g").remove();
    d3.select(this.divName + " defs").remove();
}
