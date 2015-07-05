define(['renderer', 'camera'], function(renderer, camera) {
    console.log(renderer,camera);
  // return  new THREE.TrackballControls( camera, renderer.domElement );
    return  new THREE.OrbitControls( camera, renderer.domElement );
});
