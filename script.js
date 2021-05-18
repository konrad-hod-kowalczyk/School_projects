let car = document.querySelector('.car')
let t = 0
let l = 0
document.addEventListener('keydown', function(event) {
    if(event.key == "w") {
		t+=5
        car.style.top=t+"px";
    }
    else if(event.key == "a") {
		l-=5
        car.style.left=l+"px";
    }
	else if(event.key == "s") {
		t-=5
        car.style.top=t+"px";
    }
	else if(event.key == "d") {
		l+=5
        car.style.left=l+"px";
    }
});