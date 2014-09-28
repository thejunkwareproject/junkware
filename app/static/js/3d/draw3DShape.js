var stats, controls;
var axisContainer, axisRenderer, axisScene, axisCamera, axis;

var renderer, scene, camera, particles, ambientLight, light;
var object, geometry, material, box;
var materialLib;

//camera
var SCREEN_WIDTH = window.innerWidth,
    SCREEN_HEIGHT = window.innerHeight,
    ASPECT = SCREEN_WIDTH / SCREEN_HEIGHT
    DEPTH = 600, 
    NEAR = .1, 
    FAR = 5000, 
    VIEW_ANGLE = 45;

// scene
var backgroundColor ="#000"

var initThree = function(){

    // stats
        stats = new Stats();
        stats.setMode(1); // 0: fps, 1: ms
        stats.domElement.style.position = 'absolute';
        stats.domElement.style.left = '0px';
        stats.domElement.style.bottom = '0px';
        document.body.appendChild( stats.domElement );

        stats.begin()

    //scene
        scene = new THREE.Scene();

    // camera
        camera = new THREE.PerspectiveCamera( VIEW_ANGLE, ASPECT, NEAR, FAR);
        camera.position.z = 2000;
        camera.position.set( 0, 0, DEPTH );
        camera.updateProjectionMatrix();

    //renderer
        renderer = new THREE.WebGLRenderer({
            antialias:true,
             alpha: false
         });
        renderer.setSize( SCREEN_WIDTH, SCREEN_HEIGHT );
        renderer.setClearColor(0x000000, 1.0);
        renderer.shadowMapEnabled = true;
        renderer.shadowMapSoft = true;
        renderer.shadowMapAutoUpdate = true;

        // renderer.shadowMapDebug = true;

        document.getElementById("supershapes").appendChild(renderer.domElement);

    // LIGHTS
        // ambientLight = new THREE.AmbientLight( 0xffffff );
        // scene.add( ambientLight );

        var spotLight = new THREE.SpotLight( 0xffffff );
        spotLight.shadowCameraVisible = false;
        // spotLight.castShadow = true;

        // spotLight.position.set( 100, 1000, 100 );
        // // spotLight.target.position.set(0, 0, 0);

        // spotLight.shadowMapWidth = 1000;
        // spotLight.shadowMapHeight = 1000;

        // // spotLight.shadowCameraNear = 450;; 
        // // spotLight.shadowCameraFar = camera.far;
        // // spotLight.shadowBias = 0.3;

        // spotLight.shadowDarkness = 0.8;
        // scene.add(spotLight);

        // var spotLight2 = new THREE.SpotLight();
        // // spotLight2.castShadow = true;
        // spotLight2.position.set( -170, 330, 160 );
        // scene.add(spotLight2);

    // reference

        //mouse
        controls = new THREE.TrackballControls( camera, renderer.domElement );
}

var updateCamera = function() {

    // create object bounding box
    object.scene.geometry.computeBoundingBox();
    box = object.scene.geometry.boundingBox;

    var distance = box.distanceToPoint( camera.position);
    // get the biggest of 3 dimensions
    var height=Math.max.apply(Math,box.size().toArray());
    var fov = 2 * Math.atan( height / ( 2 * distance ) ) * ( 180 / Math.PI );

    // adjust camera to object
    camera.fov=fov;
    camera.updateProjectionMatrix();
}

var cloneObject = function () {
    var clone=object.scene.clone();
    clone.position.set(random(0,100),random(0,100),random(0,100));
    scene.add(clone);
}

var objectHearthBeat = function  (_scale) {
    object.scene.scale.x = random(1,1+_scale);
    object.scene.scale.y = random(1,1+_scale);
    object.scene.scale.z = random(1,1+_scale);
}

var AXIS_CANVAS_WIDTH=100, AXIS_CANVAS_HEIGHT=100;

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

/*var mouseDown=false;
function addEventListeners() {
    callbacks = {
        onMouseDown: function (a) {
            mouseDown = true;
            lastMouseX = a.clientX;
            lastMouseY = a.clientY;
        },
        onMouseUp: function (a) {
            mouseDown = false;
        },
        onMouseMove: function (c) {
            if (mouseDown) {
                var b = c.clientX;
                var a = c.clientY;
                rotX = object.scene.rotation.x += (a - lastMouseY) * 0.01;
                rotY = object.scene.rotation.y += (b - lastMouseX) * 0.01;
                lastMouseY = a;
                lastMouseX = b;
            }
        },
        onDblClick: function () {
            rotX = object.scene.rotation.x = 0;
            rotY = object.scene.rotation.y = 0;
        }
    };
    document.getElementById("supershapes").onmousedown = callbacks.onMouseDown;
    document.getElementById("supershapes").onmouseup = callbacks.onMouseUp;
    document.getElementById("supershapes").onmousemove = callbacks.onMouseMove;
    document.getElementById("supershapes").ondblclick = callbacks.onDblClick;
    document.getElementById("supershapes").onkeydown = callbacks.onKeyDown;
    document.getElementById("supershapes").addEventListener("mousewheel", MouseWheelHandler, false);
 
    function MouseWheelHandler(e) {
        camera.position.z += -e.wheelDelta/120*50;
    } 
};*/


function render () {
    renderer.render(scene, camera);
    axisRenderer.render( axisScene, axisCamera );
}

function animate() {

    requestAnimationFrame( animate );
    controls.update();

    axisCamera.position.copy( camera.position );
    axisCamera.position.sub( controls.target ); // added by @libe
    // axisCamera.position.setLength( CAM_DISTANCE );

    axisCamera.lookAt( axisScene.position );
    render();

    stats.update();
}

// setInterval(function () {
//     objectHearthBeat(.01);
// }, 150)

initThree();
initAxis();
// addEventListeners();
object = new meshObject(0, 0);
object.update();
updateCamera();
console.log(object);
animate();
