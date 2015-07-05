define(function() {
  var WIDTH = window.innerWidth-250;
  var HEIGHT = window.innerHeight-120;
  var AXIS_CANVAS_WIDTH = 100;
  var AXIS_CANVAS_HEIGHT = 100;

  return {
    width: WIDTH,
    height: HEIGHT,
    axisWidth : 100,
    axisHeight : 100,
    aspect: WIDTH / HEIGHT,
    viewAngle: 45,
    near: .1,
    far: 1000,
    phiSteps: 200,
    thetaSteps:200
  };
});
