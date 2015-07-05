
include <supershape.scad>

create_supershape();

module create_supershape()
{
    scale([10,10,10])
    RenderSuperShape(
        shape1=supershape(m=15, n1=18, n2=0, n3=17, a=1, b=1),
        shape2=supershape(m=16, n1=9, n2=16, n3=41, a=1, b=1),
        phisteps = 8,
        thetasteps = 64,
        points=false,
        pointcolor=[1,1,1],
        wireframe=false,
        faces=true);

}
