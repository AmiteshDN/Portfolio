// dynamic software text
var i = 0;
var txt = '<Software>'; //test to come dynamically
var speed = 150;    //speed between each text in ms

function typeWriter() {
    if (i < txt.length) {   //char starting from 0 to length of the text
        document.getElementById("software").innerHTML += txt.charAt(i); //add each char to the tag 
        i++; //go to net char
        setTimeout(typeWriter, speed); //set timeout between each function call
    }
}
// set the function on page load
document.getElementsByTagName("body").onload = typeWriter();




