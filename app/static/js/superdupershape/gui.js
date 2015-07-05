define(function() {

 // console.log(junk.shape);

  var settings = {
    t1: {min: -2, max: 2},
    d1: {min: -2, max: 2},
    m1: {min: 0, max: 20},
    n11: {min: 0, max: 100},
    n12: {min: 0, max: 100},
    n13: {min: 0, max: 100},
    t2: {min: -2, max: 2},
    d2: {min: -2, max: 2},
    n21: {min: 0, max: 100},
    n22: {min: 0, max: 100},
    n23: {min: 0, max: 100},
    m2: {min: 0, max: 100},
    c1: {min: 0, max: 8},
    c2: {min: 0, max: 8},
    c3: {min: 0, max: 8},
    export_to_STL: "export to clean STL"
  };

  var controls = new function() {

    this.t1 = 0;
    this.d1 = 0;
    this.m1 = junk.shape.m1; 
    this.n11 = junk.shape.n11; 
    this.n12 = junk.shape.n12;
    this.n13 = junk.shape.n13;


    this.t2 = 0;
    this.d2 = 0;
    this.m2 = junk.shape.m2;
    this.n21 = junk.shape.n21;
    this.n22 = junk.shape.n22;
    this.n23 = junk.shape.n23;

    this.c1 = 2;
    this.c2 = 4;
    this.c3 = 1;
    this.export_to_STL = function() {
      console.log("export to STL (may take some time)");
      console.log(JSON.stringify(this));
      var url = "/data/toStl/" + window.location.pathname.split("/")[2];
      console.log(url);
      $.post(url , {"shape" : JSON.stringify(this)}, function(data){
        console.log("ok ");
      //  console.log(data);
        uriContent = 'data:Application/octet-stream;download=' + window.location.pathname.split("/")[2]+".stl,"+encodeURIComponent(data);
        // console.log(uriContent);
        document.location = uriContent;
      })
    }
  };
  
  var gui = new dat.GUI({load:
      {
        "preset": "Default",
        "closed": true,
        "folders": {}
      }
      });

  for (var i in settings) {
    var s = settings[i];
    // console.log(s);
    gui.add(controls, i, s.min, s.max).listen().onChange(update);
  }


  var listeners = [];

  function update () {
    listeners.forEach(function  (listener) {
      listener(controls);
    })

    junk.shape.m1=controls.m1;
    junk.shape.n11=controls.n11;
    junk.shape.n12=controls.n12;
    junk.shape.n13=controls.n13;
    junk.shape.m2=controls.m2;
    junk.shape.n21=controls.n21;
    junk.shape.n22=controls.n22;
    junk.shape.n23=controls.n23;

  }

  // gui.remember(controls);

  return {
    onChange: function  (func) {
      listeners.push(func);
    },
    controls: controls
  }

});
