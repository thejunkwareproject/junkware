
include <supershape.scad>

create_supershape();

module create_supershape()
{
    scale([10,10,10])
    RenderSuperShape(
        shape1=supershape(m=5, n1=203, n2=531.075359865, n3=303.471634208, a=1, b=1),
        shape2=supershape(m=7, n1=368, n2=561, n3=75.8679085521, a=1, b=1),
        phisteps = 8,
        thetasteps = 64,
        points=false,
        pointcolor=[1,1,1],
        wireframe=false,
        faces=true);

}
