
include <supershape.scad>

create_supershape();

module create_supershape()
{
    scale([10,10,10])
    RenderSuperShape(
        shape1=supershape(m=4.11854360711, n1=182, n2=704, n3=919, a=1, b=1),
        shape2=supershape(m=4, n1=161, n2=21.6765453006, n3=454, a=1, b=1),
        phisteps = 8,
        thetasteps = 64,
        points=false,
        pointcolor=[1,1,1],
        wireframe=false,
        faces=true);

}
