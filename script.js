let car = document.querySelector('.car')
let walls = document.querySelectorAll('.wall')
let posx = 0
let posy = 0
let change = 5
let angle = 0
//document.querySelector('.car #ct').style.background = '#00ff00';
document.addEventListener('keydown', function(event) {
    let map = {}
	map[event.key] = event.type == 'keydown';
	let pos=car.getBoundingClientRect();
	for(let i=0;i<walls.length;i++)
	{
		let w_pos = walls[i].getBoundingClientRect();
		if(overlaps(pos,w_pos))
		{
			document.querySelector('.car #ct').style.background = '#00ff00';
			break;
		}
		if(i==walls.length-1) 
		{
			document.querySelector('.car #ct').style.background = '#cc6b4d';
		}
	}
	if(event.key == "w") {
		posx-=change*Math.cos(angle+Math.PI)
		posy-=change*-Math.sin(angle+Math.PI)
		car.style.top=posx+"px";
		car.style.left=posy+"px";
	}
	if(event.key == "a") {
		angle-=0.1;
		angle=angle%(2*Math.PI);
		car.style.transform="rotate("+(angle+Math.PI)+"rad) scaleY(0.5) scaleX(0.5)";
	}
	if(event.key == "s") {
		posx+=change*Math.cos(angle+Math.PI)
		posy+=change*-Math.sin(angle+Math.PI)
		car.style.top=posx+"px";
		car.style.left=posy+"px";
	}
	if(event.key == "d") {
		angle+=0.1;
		angle=angle%(2*Math.PI);
		car.style.transform="rotate("+(angle+Math.PI)+"rad) scaleY(0.5) scaleX(0.5)";
	}
});
function overlaps(a,b)
{
	return (a.x>b.x && a.x<b.x+b.width && a.y>b.y && a.y<b.y+b.height) || (a.x+a.width>b.x && a.x+a.width<b.x+b.width && a.y>b.y && a.y<b.y+b.height) || (a.x>b.x && a.x<b.x+b.width && a.y+a.height>b.y && a.y+a.height<b.y+b.height) || (a.x+a.width>b.x && a.x+a.width<b.x+b.width && a.y+a.height>b.y && a.y+a.height<b.y+b.height);
}