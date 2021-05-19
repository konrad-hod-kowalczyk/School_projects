let car = document.querySelector('.car')
let posx = 0
let posy = 0
let change = 5
let angle = 0
document.addEventListener('keydown', function(event) {
    if(event.key == "w") {
		posx-=change*Math.cos(angle+Math.PI)
		posy-=change*-Math.sin(angle+Math.PI)
        car.style.top=posx+"px";
		car.style.left=posy+"px";
    }
    if(event.key == "a") {
		angle-=0.1
        car.style.transform="rotate("+(angle+Math.PI)+"rad) scaleY(0.5) scaleX(0.5)";
    }
	if(event.key == "s") {
		posx+=change*Math.cos(angle+Math.PI)
		posy+=change*-Math.sin(angle+Math.PI)
        car.style.top=posx+"px";
		car.style.left=posy+"px";
    }
	if(event.key == "d") {
		angle+=0.1
		car.style.transform="rotate("+(angle+Math.PI)+"rad) scaleY(0.5) scaleX(0.5)";
    }
});