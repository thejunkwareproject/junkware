var axisContainer, axisRenderer, axisScene, axisCamera, axis;

var initAxis= function() {

    // dom
    axisContainer = document.getElementById('three-axis');

    // renderer
    axisRenderer = new THREE.CanvasRenderer();
    axisRenderer.setSize( AXIS_CANVAS_WIDTH, AXIS_CANVAS_HEIGHT );
    axisContainer.appendChild( axisRenderer.domElement );

    // scene
    axisScene = new THREE.Scene();

    // camera
    axisCamera = new THREE.PerspectiveCamera( 50, AXIS_CANVAS_WIDTH / AXIS_CANVAS_HEIGHT, 1, 1000 );
    axisCamera.up = camera.up; // important!

    // axes
    axis = new THREE.AxisHelper( 100 );
    axisScene.add( axis );
}
