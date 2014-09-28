var a1=1, a2=1, b=1, xx, step=0.05, yy, zz, n1=4, n2=12, n3=15, n4=15, r, raux1, r1, raux2, r2;
var N_X = Math.floor(2*Math.PI/step);
var N_Y = Math.floor(Math.PI/step);
var color = "0xffffff";
var pSize=5, opac=1;

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
    N_X = parseInt(2 * Math.PI / step + 1.3462);
    N_Y = parseInt(Math.PI / step + 1.5);
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

function meshObject(b, a) {
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
    this.createMeshGeometry();
    this.createMeshMaterial()
    this.material = getRandomMaterial();

}

meshObject.prototype.createMeshGeometry = function () {

    geometry = new THREE.Geometry();
    geometry.dynamic = true;
    step = 0.05;

    N_X = parseInt(2 * Math.PI / step + 1.3462);
    N_Y = parseInt(Math.PI / step + 1.5);

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

    for (var u = 0; u < (N_X - 1); u++) {
        for (var s = 0; s < (N_Y - 1); s++) {
            var d = u * N_Y + s;
            var c = u * N_Y + s + 1;
            var b = (u + 1) * N_Y + s + 1;
            var a = (u + 1) * N_Y + s;
            geometry.faces.push(new THREE.Face3(d, c, b))
            geometry.faces.push(new THREE.Face3(c, b, a))
            geometry.faces.push(new THREE.Face3(a, d, c))
        }
    }
    geometry.computeFaceNormals();
    geometry.computeVertexNormals();
    // geometry.computeCentroids();
};

meshObject.prototype.createMeshMaterial = function () {
    this.scene = new THREE.Mesh(geometry, this.material);
    this.scene.doubleSided = true;
    this.scene.castShadow = true;
    this.scene.receiveShadow = true;
    scene.add(this.scene);
    this.scene.rotation.x = this.rotX;
    this.scene.rotation.y = this.rotY
};

meshObject.prototype.update = function () {
    this.createMeshGeometry();
    // material.ambient.setHex(color);
    this.scene.geometry.vertices = geometry.vertices;
    this.scene.rotation.x = this.rotX;
    this.scene.rotation.y = this.rotY
    this.scene.geometry.verticesNeedUpdate = true
};


function getMaterialLib(){

    var texture = THREE.ImageUtils.loadTexture('/img/texture.png');
    texture.repeat.set(10, 10);
    texture.wrapS = texture.wrapT = THREE.RepeatWrapping;
    texture.anisotropy = 16;
    texture.needsUpdate = true;

    var textureBump = THREE.ImageUtils.loadTexture('/img/bump.png');
    textureBump.repeat.set(10, 10);
    textureBump.wrapS = textureBump.wrapT = THREE.RepeatWrapping;
    textureBump.anisotropy = 16;
    textureBump.needsUpdate = true;
    
    return {
      '1':   new THREE.MeshBasicMaterial({ color: getRandomColor() }),
      '2':   new THREE.MeshLambertMaterial({ color: getRandomColor() }),
      '3':   new THREE.MeshPhongMaterial({ color: getRandomColor() }),

      '4':   new THREE.MeshBasicMaterial({ color: getRandomColor(), opacity: 0.5, transparent: true }),
      '5':   new THREE.MeshLambertMaterial({ color: getRandomColor(), opacity: 0.5, transparent: true }),
      '6':   new THREE.MeshPhongMaterial({ color: getRandomColor(), opacity: 0.5, transparent: true }),

      '7':   new THREE.MeshLambertMaterial({ color: 0xff0000, ambient: 0xffffff }),
      '8':   new THREE.MeshLambertMaterial({ color: 0xff0000, emissive: 0x000088 }),

      '9':   new THREE.MeshPhongMaterial({ color: 0xff0000, ambient: 0x3ffc33 }),
      '10':  new THREE.MeshPhongMaterial({ color: 0xff0000, emissive: 0x000088 }),
      '11':  new THREE.MeshPhongMaterial({ color: 0xff0000, emissive: 0x004000, specular: 0x0022ff }),
      '12':  new THREE.MeshPhongMaterial({ color: 0xff0000, specular: 0x0022ff, shininess: 3 }),

      '13':  new THREE.MeshLambertMaterial({ map: texture, color: 0xff0000, ambient: 0x3ffc33 }),
      '14':  new THREE.MeshLambertMaterial({ map: texture, color: 0xff0000, emissive: 0x000088 }),
      '15':  new THREE.MeshLambertMaterial({ map: texture, color: 0xff0000, emissive: 0x004000, specular: 0x0022ff }),
      '16':  new THREE.MeshLambertMaterial({ map: texture, color: 0xff0000, specular: 0x0022ff, shininess: 3 }),

      '17':  new THREE.MeshPhongMaterial({ map: texture, color: 0xff0000, ambient: 0x3ffc33 }),
      '18':  new THREE.MeshPhongMaterial({ map: texture, color: 0xff0000, emissive: 0x000088 }),
      '19':  new THREE.MeshPhongMaterial({ map: texture, color: 0xff0000, emissive: 0x004000, specular: 0x0022ff }),
      '20':  new THREE.MeshPhongMaterial({ map: texture, color: 0xff0000, specular: 0x0022ff, shininess: 3 }),

      '21':  new THREE.MeshPhongMaterial({ map: texture, bumpMap: textureBump, color: 0xff0000, ambient: 0x3ffc33 }),
      '22':  new THREE.MeshPhongMaterial({ map: texture, bumpMap: textureBump, color: 0xff0000, emissive: 0x000088 }),
      '23':  new THREE.MeshPhongMaterial({ map: texture, bumpMap: textureBump, color: 0xff0000, emissive: 0x004000, specular: 0x0022ff }),
      '24':  new THREE.MeshPhongMaterial({ map: texture, bumpMap: textureBump, color: 0xff0000, specular: 0x0022ff, shininess: 3 }),
    }
}

function getRandomMaterial() {
    var materialLib=getMaterialLib();
    return materialLib[parseInt(random(1,24)).toString()]
}

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
