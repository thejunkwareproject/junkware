var shapeData;

requirejs(['camera', 'renderer','scene', 'mesh', "gui", 'stats', 'controls', 'settings'], function(camera, renderer, scene, Mesh, gui,stats, controls,settings) {
  if (!Detector.webgl) {
    Detector.addGetWebGLMessage();
    return;
  }

  // additional axis
  console.log(settings.axisHeight);
  var axisContainer, axisRenderer, axisScene, axisCamera, axis;
  function initAxis() {
      // dom
      axisContainer = document.getElementById('three-axis');

      // renderer
      axisRenderer = new THREE.CanvasRenderer();
      axisRenderer.setSize( settings.axisWidth, settings.axisHeight );
      axisContainer.appendChild( axisRenderer.domElement );

      // scene
      axisScene = new THREE.Scene();

      // camera
      axisCamera = new THREE.PerspectiveCamera( 50, settings.axisWidth / settings.axisHeight, 1, 1000 );
      axisCamera.up = camera.up; // important!

      // axes
      axis = new THREE.AxisHelper( 100 );
      axisScene.add( axis );
  }

  // console.log(controls);
  
  // controls.target.z = 150;
  shapeData=gui.controls;

  initAxis();
  var mesh = new Mesh(gui.controls);
  gui.onChange(mesh.update.bind(mesh));
  // eventHandler.init(mesh);

  // LIGHTS
  // ambientLight = new THREE.AmbientLight( 0xffffff );
  // ambientLight.castShadow = true;
  // scene.add( ambientLight );

  var spotLight = new THREE.SpotLight( 0xffffff );
  spotLight.shadowCameraVisible = false;

  spotLight.position.set( 100, 500, 100 );
  spotLight.target.position.set(0, 0, 0);

  spotLight.shadowMapWidth = 1000;
  spotLight.shadowMapHeight = 1000;

  spotLight.shadowCameraNear = 450;; 
  spotLight.shadowCameraFar = camera.far;
  spotLight.shadowBias = 0.3;

  spotLight.shadowDarkness = 0.8;
  spotLight.castShadow = true;

  // spotLight.shadowCameraVisible = true;

  scene.add(spotLight);

  THREEx.WindowResize.bind(renderer, camera);

  scene.add(camera);
  animate();

  function animate() {
    controls.update();
    requestAnimationFrame(animate);

    axisCamera.position.copy( camera.position );
    // axisCamera.position.sub( controls.target ); // added by @libe
    axisCamera.lookAt( axisScene.position );

    render();
    stats.update();
  }

  setInterval(function () {
    objectHearthBeat(.1);
  }, 1000)

  var objectHearthBeat = function  (_scale) {
    console.log(scene.scale);
    scene.scale.x = random(1,1+_scale);
    scene.scale.y = random(1,1+_scale);
    scene.scale.z = random(1,1+_scale);
  }

  function render() {
    renderer.clear();
    renderer.render(scene, camera);
    axisRenderer.clear();
    axisRenderer.render( axisScene, axisCamera );

  }



});
