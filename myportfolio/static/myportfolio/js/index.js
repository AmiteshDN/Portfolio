var i = 0;
var txt = '<Software>';
var speed = 150;

document.getElementsByTagName("body").onload = typeWriter();

function typeWriter() {
    console.log(i)
    if (i < txt.length) {
        document.getElementById("software").innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
        console.log("hello");
    }
}
