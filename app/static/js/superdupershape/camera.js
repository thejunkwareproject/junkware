define(['settings'], function(settings) {

  var camera =
    new THREE.PerspectiveCamera(
      settings.viewAngle,
      settings.aspect,
      settings.near,
      settings.far);

    camera.updateProjectionMatrix();

  camera.position.z = 300;
  return camera;
});
