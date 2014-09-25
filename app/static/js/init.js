
var stats;

var renderer, scene, camera, particles, ambientLight, light;
var backgroundColor ="#000"
var DEPTH = 600, NEAR = 1, FAR = 4000, VIEW_ANGLE = 45;

var object, geometry;

var initThree = function(){
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera( 20, window.innerWidth / window.innerHeight, 0.1, 5000 );
    camera.position.z = 2000;
 
    renderer = new THREE.WebGLRenderer();
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.getElementById("supershapes").appendChild(renderer.domElement);
    renderer.setClearColor(0x000000, 1.0);
 
    var spotLight = new THREE.SpotLight();
    spotLight.position.set( 170, 330, -160 );
    scene.add(spotLight);
 
    var spotLight2 = new THREE.SpotLight();
    spotLight2.position.set( -170, 330, 160 );
    scene.add(spotLight2);
 
 
    geometry = new THREE.Geometry();
    geometry.dynamic = true;

    stats = new Stats();
    stats.setMode(1); // 0: fps, 1: ms

    // Align top-left
    stats.domElement.style.position = 'absolute';
    stats.domElement.style.left = '0px';
    stats.domElement.style.bottom = '0px';
    document.body.appendChild( stats.domElement );

    stats.begin();
};

var mouseDown=false;
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
};

function animate() {
    requestAnimationFrame( animate );
    renderer.render(scene, camera);
    stats.update();
}

initThree();
addEventListeners();
object = new pointCloudObject(0, 46.4);
console.log(object);
object.update();
animate();
