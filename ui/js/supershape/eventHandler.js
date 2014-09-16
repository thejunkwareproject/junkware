function addEventListeners() {
    callbacks = {
        onMouseDown: function (a) {
            mouseDown = true;
            lastMouseX = a.clientX;
            lastMouseY = a.clientY
        },
        onMouseUp: function (a) {
            mouseDown = false
        },
        onMouseMove: function (c) {
            if (mouseDown) {
                var b = c.clientX;
                var a = c.clientY;
                rotX = object.scene.rotation.x += (a - lastMouseY) * 0.01;
                rotY = object.scene.rotation.y += (b - lastMouseX) * 0.01;
                lastMouseY = a;
                lastMouseX = b
            }
        },
        onDblClick: function () {
            rotX = object.scene.rotation.x = 0;
            rotY = object.scene.rotation.y = 0
        }
    };
    document.getElementById("supershapes").onmousedown = callbacks.onMouseDown;
    document.getElementById("supershapes").onmouseup = callbacks.onMouseUp;
    document.getElementById("supershapes").onmousemove = callbacks.onMouseMove;
    document.getElementById("supershapes").ondblclick = callbacks.onDblClick;
    document.getElementById("supershapes").onkeydown = callbacks.onKeyDown;
};
