// SLIDER
var slideIndex = 1;
showSlides(slideIndex);
// setInterval(AutoSlider, 5000, 1);
//
// function AutoSlider(n){
// 	showSlides(slideIndex += n);
// }

function plus(n){
	showSlides(slideIndex += n);
}

function showSlides(n){
	var i;
	var slides = document.getElementsByClassName("slide");

	if(n > slides.length){
		slideIndex = 1;
	}else if(n < 1){
		slideIndex = slides.length;
	}
	for(i=0; i < slides.length; i++){
		slides[i].style.display = "none";
	}
	slides[slideIndex-1].style.display = "block";
}

