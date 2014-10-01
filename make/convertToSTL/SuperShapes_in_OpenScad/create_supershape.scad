include <supershape.scad>

create_supershape();

module create_supershape()
{
	scale([10,10,10])
	RenderSuperShape(
		shape1=supershape(m=18, n1=60, n2=55, n3=1000, a=1, b=1), 
		shape2=supershape(m=6, n1=220, n2=100, n3=100, a=1, b=1), 
		phisteps = 8,
		thetasteps = 64,
		points=false,
		pointcolor=[1,1,1],
		wireframe=false,
		faces=true);

}
