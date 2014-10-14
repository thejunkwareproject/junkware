define(['renderer', 'camera'], function(renderer, camera) {
    console.log(renderer,camera);
  return  new THREE.TrackballControls( camera, renderer.domElement );
});
