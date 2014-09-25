var a1=1, a2=1, b=1, xx, step=0.05, yy, zz, n1=4, n2=12, n3=15, n4=15, r, raux1, r1, raux2, r2;
var N_X = Math.floor(2*Math.PI/step);
var N_Y = Math.floor(Math.PI/step);
var color = "0xffffff";
var pSize=5, opac=1;

var random = function(min, max){
    return min + Math.random()*(max-min);
};

function pointCloudObject(b, a) {
    a1 = random(0, 2);
    a2 = random(0, 2);
    b = random(0, 2);
    //n1 = random(0, 20);
    n2 = random(0, 2.5);
    n3 = random(0, 2.5);
    n4 = random(0, 10);
    //step = random(0.02, 0.9);

    this.rotX = b;
    this.rotY = a;
    this.scene = new THREE.Object3D();
    this.createPointCloudGeometry();
    this.createPointCloudMaterial()
}

pointCloudObject.prototype.createPointCloudGeometry = function () {

    geometry = new THREE.Geometry();
    geometry.dynamic = true;
 
    for (var x=0; x<N_X; x++){
        var i = -Math.PI + x*step;
        for (var y=0; y<N_Y; y++) {
            var j = -Math.PI/2.0 + y*step;
            raux1=Math.pow(Math.abs(1/a1*Math.abs(Math.cos(n1*i/4))), n3)+Math.pow(Math.abs(1/a2*Math.abs(Math.sin(n1*i/4))), n4);
            r1=Math.pow(Math.abs(raux1), (-1/n2));
            raux2=Math.pow(Math.abs(1/a1*Math.abs(Math.cos(n1*j/4))), n3)+Math.pow(Math.abs(1/a2*Math.abs(Math.sin(n1*j/4))), n4);
            r2=Math.pow(Math.abs(raux2), (-1/n2));
            xx=r1*Math.cos(i)*r2*Math.cos(j)*100;
            yy=r1*Math.sin(i)*r2*Math.cos(j)*100;
            zz=r2*Math.sin(j)*100;
 
            geometry.vertices.push(new THREE.Vector3(xx, yy, zz));
        }
    }
};

pointCloudObject.prototype.update = function () {
    this.createPointCloudGeometry();
    material.opacity = opac;
    material.color.setHex(color);
    this.scene.geometry.vertices = geometry.vertices;
    this.scene.rotation.x = this.rotX;
    this.scene.rotation.y = this.rotY
    this.scene.geometry.verticesNeedUpdate = true;
};

pointCloudObject.prototype.createPointCloudMaterial = function () {
    material = new THREE.PointCloudMaterial({
        size: pSize,
        color: color,
        blending: THREE.AdditiveBlending,
        transparent: true
    });
    this.scene = new THREE.PointCloud(geometry, material);
    this.scene.castShadow = true;
    scene.add(this.scene);
    this.scene.rotation.x = this.rotX;
    this.scene.rotation.y = this.rotY
};
