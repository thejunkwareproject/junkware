var shapeData;

requirejs(['camera', 'renderer','scene', 'mesh', 'gui', 'stats', 'controls'], function(camera, renderer, scene, Mesh, gui, stats, controls) {
  if (!Detector.webgl) {
    Detector.addGetWebGLMessage();
    return;
  }

  console.log(controls);

  shapeData=gui.controls;
  // console.log(gui.controls);

  var mesh = new Mesh(gui.controls);
  gui.onChange(mesh.update.bind(mesh));
  // eventHandler.init(mesh);

  THREEx.WindowResize.bind(renderer, camera);

  scene.add(camera);
  animate();

  function animate() {
    // controls.update();
    requestAnimationFrame(animate);
    // axisCamera.position.sub( controls.target ); // added by @libe
    render();
    stats.update();
  }

  function render() {
    renderer.clear();
    renderer.render(scene, camera);
  }

});
