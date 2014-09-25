var moleculeCamera, moleculeScene, moleculeRenderer;
var moleculeControls;
var moleculeRoot;

var moleculeObjects = [];
var tmpVec1 = new THREE.Vector3();
var tmpVec2 = new THREE.Vector3();
var tmpVec3 = new THREE.Vector3();
var tmpVec4 = new THREE.Vector3();

var MOLECULES_CANVAS_WIDTH=200,
     MOLECULES_CANVAS_HEIGHT=150;
var loader = new THREE.PDBLoader();
var colorSpriteMap = {};
var baseSprite = document.createElement( 'img' );

/*var MOLECULES = {
    "Ethanol": "ethanol.pdb",
    "Aspirin": "aspirin.pdb",
    "Caffeine": "caffeine.pdb",
    "Nicotine": "nicotine.pdb",
    "LSD": "lsd.pdb",
    "Cocaine": "cocaine.pdb",
    "Cholesterol": "cholesterol.pdb",
    "Lycopene": "lycopene.pdb",
    "Glucose": "glucose.pdb",
    "Aluminium oxide": "Al2O3.pdb",
    "Cubane": "cubane.pdb",
    "Copper": "cu.pdb",
    "Fluorite": "caf2.pdb",
    "Salt": "nacl.pdb",
    "YBCO superconductor": "ybco.pdb",
    "Buckyball": "buckyball.pdb",
    //"Diamond": "diamond.pdb",
    "Graphite": "graphite.pdb"
};*/


var getRandomMolecule = function(callback) {
    $.get("/data/molecules", function (data) {

        console.log(data);
        var mol = data.molecules[ parseInt(random(0,data.molecules.length))];
        console.log(mol);
        callback(mol);
    })
}

function initMolecule() {


    moleculeCamera = new THREE.PerspectiveCamera( 70, MOLECULES_CANVAS_WIDTH / MOLECULES_CANVAS_HEIGHT, 1, 5000 );
    moleculeCamera.position.z = 500;

    moleculeScene = new THREE.Scene();

    moleculeRoot = new THREE.Object3D();
    moleculeScene.add( moleculeRoot );

    // renderer
    moleculeRenderer = new THREE.CSS3DRenderer();
    moleculeRenderer.setSize( MOLECULES_CANVAS_WIDTH, MOLECULES_CANVAS_HEIGHT );
    document.getElementById( 'molecules' ).appendChild( moleculeRenderer.domElement );

    // controls
    moleculeControls = new THREE.TrackballControls( moleculeCamera, moleculeRenderer.domElement );
    moleculeControls.rotateSpeed = 0.5;
    moleculeControls.addEventListener( 'change', moleculeRenderer );

    // load molecules

    getRandomMolecule(function(moleculeFile) {
        var url = "/data/molecules/" + moleculeFile;
        baseSprite.onload = function () {
            loadMolecule( url );
        };

        baseSprite.src = '/img/ball.png';

    });

}

function colorify( ctx, width, height, color, a ) {


    var r = color.r;
    var g = color.g;
    var b = color.b;
    console.log(r,g,b);
    var imageData = ctx.getImageData( 0, 0, width, height );
    var data = imageData.data;

    for ( var y = 0; y < height; y ++ ) {

        for ( var x = 0; x < width; x ++ ) {

            var index = ( y * width + x ) * 4;

            data[ index ]     *= r;
            data[ index + 1 ] *= g;
            data[ index + 2 ] *= b;
            data[ index + 3 ] *= a;

        }

    }

    ctx.putImageData( imageData, 0, 0 );
}

function imageToCanvas( image ) {

    var width = image.width;
    var height = image.height;

    var canvas = document.createElement( 'canvas' );

    canvas.width = width;
    canvas.height = height;

    var context = canvas.getContext( '2d' );
    context.drawImage( image, 0, 0, width, height );

    return canvas;
}

function loadMolecule( url ) {

    for ( var i = 0; i < moleculeObjects.length; i ++ ) {
        var moleculeObject = moleculeObjects[ i ];
        moleculeObject.parent.remove( moleculeObject );
    }

    moleculeObjects = [];

    loader.load( url, function ( geometry, geometryBonds ) {

        var offset = geometry.center();
        geometryBonds.applyMatrix( new THREE.Matrix4().makeTranslation( offset.x, offset.y, offset.z ) );

        for ( var i = 0; i < geometry.vertices.length; i ++ ) {

            var position = geometry.vertices[ i ];
            var color = geometry.colors[ i ];
            var element = geometry.elements[ i ];

            if ( ! colorSpriteMap[ element ] ) {

                var canvas = imageToCanvas( baseSprite );
                var context = canvas.getContext( '2d' );
                // console.log(color);
                colorify( context, canvas.width, canvas.height, color, 1 );

                var dataUrl = canvas.toDataURL();

                colorSpriteMap[ element ] = dataUrl;

            }

            colorSprite = colorSpriteMap[ element ];

            var atom = document.createElement( 'img' );
            atom.src = colorSprite;

            var moleculeObject = new THREE.CSS3DSprite( atom );
            moleculeObject.position.copy( position );
            moleculeObject.position.multiplyScalar( 75 );

            moleculeObject.matrixAutoUpdate = false;
            moleculeObject.updateMatrix();

            moleculeRoot.add( moleculeObject );

            moleculeObjects.push( moleculeObject );

        }

        for ( var i = 0; i < geometryBonds.vertices.length; i += 2 ) {

            var start = geometryBonds.vertices[ i ];
            var end = geometryBonds.vertices[ i + 1 ];

            start.multiplyScalar( 75 );
            end.multiplyScalar( 75 );

            tmpVec1.subVectors( end, start );
            var bondLength = tmpVec1.length() - 50;


            //

            var bond = document.createElement( 'div' );
            bond.className = "bond";
            bond.style.height = bondLength + "px";

            var moleculeObject = new THREE.CSS3DObject( bond );
            moleculeObject.position.copy( start );
            moleculeObject.position.lerp( end, 0.5 );

            moleculeObject.userData.bondLengthShort = bondLength + "px";
            moleculeObject.userData.bondLengthFull = ( bondLength + 55 ) + "px";

            //

            var axis = tmpVec2.set( 0, 1, 0 ).cross( tmpVec1 );
            var radians = Math.acos( tmpVec3.set( 0, 1, 0 ).dot( tmpVec4.copy( tmpVec1 ).normalize() ) );

            var objMatrix = new THREE.Matrix4().makeRotationAxis( axis.normalize(), radians );
            moleculeObject.matrix = objMatrix;
            moleculeObject.rotation.setFromRotationMatrix( moleculeObject.matrix, moleculeObject.rotation.order );

            moleculeObject.matrixAutoUpdate = false;
            moleculeObject.updateMatrix();

            moleculeRoot.add( moleculeObject );

            moleculeObjects.push( moleculeObject );

            //

            var bond = document.createElement( 'div' );
            bond.className = "bond";
            bond.style.height = bondLength + "px";

            var joint = new THREE.Object3D( bond );
            joint.position.copy( start );
            joint.position.lerp( end, 0.5 );

            joint.matrix.copy( objMatrix );
            joint.rotation.setFromRotationMatrix( joint.matrix, joint.rotation.order );

            joint.matrixAutoUpdate = false;
            joint.updateMatrix();

            var moleculeObject = new THREE.CSS3DObject( bond );
            moleculeObject.rotation.y = Math.PI/2;

            moleculeObject.matrixAutoUpdate = false;
            moleculeObject.updateMatrix();

            moleculeObject.userData.bondLengthShort = bondLength + "px";
            moleculeObject.userData.bondLengthFull = ( bondLength + 55 ) + "px";

            moleculeObject.userData.joint = joint;

            joint.add( moleculeObject );
            moleculeRoot.add( joint );

            moleculeObjects.push( moleculeObject );

        }

        //console.log( "CSS3DObjects:", moleculeObjects.length );

        renderMolecule();

    } );
}

function animateMolecule() {

    requestAnimationFrame( animateMolecule );
    // moleculeControls.update();

    var time = Date.now() * 0.0004;

    moleculeRoot.rotation.x = time;
    moleculeRoot.rotation.y = time * 0.7;

    renderMolecule();
}

function renderMolecule() {

    moleculeRenderer.render( moleculeScene, moleculeCamera );
}



initMolecule();
animateMolecule();
