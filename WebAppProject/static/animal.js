function showText(text){
    document.getElementById("text-camel").innerHTML=text;
}
function hide(){
    document.getElementById("text-camel").innerHTML="";
}

function showText2(text){
    document.getElementById("text-snake").innerHTML=text;
}
function hide2(){
    document.getElementById("text-snake").innerHTML="";
}

function showText3(text){
    document.getElementById("text-stingray").innerHTML=text;
}
function hide3(){
    document.getElementById("text-stingray").innerHTML="";
}

function showText4(text){
    document.getElementById("text-dolphin").innerHTML=text;
}
function hide4(){
    document.getElementById("text-dolphin").innerHTML="";
}

function showText5(text){
    document.getElementById("text-polar-bear").innerHTML=text;
}
function hide5(){
    document.getElementById("text-polar-bear").innerHTML="";
}

function showText6(text){
    document.getElementById("text-penguin").innerHTML=text;
}
function hide6(){
    document.getElementById("text-penguin").innerHTML="";
}

function showText7(text){
    document.getElementById("text-deer").innerHTML=text;
}
function hide7(){
    document.getElementById("text-deer").innerHTML="";
}

function showText8(text){
    document.getElementById("text-falcon").innerHTML=text;
}
function hide8(){
    document.getElementById("text-falcon").innerHTML="";
}

function filterAnimals(value) {
    //Button class code
    let buttons = document.querySelectorAll(".button-value");
    buttons.forEach((button) => {
      //check if value equals innerText
      if (value.toUpperCase() == button.innerText.toUpperCase()) {
        button.classList.add("active");
      } else {
        button.classList.remove("active");
      }
    });
  
    //select all cards
    let elements = document.querySelectorAll(".js");
    //loop through all cards
    elements.forEach((element) => {
      element.classList.add("hide")
      //display all cards on 'all' button click
      if (value == "all") {
        element.classList.remove("hide");
      } else {
        //Check if element contains category class
        if (element.classList.contains(value)) {
          //display element based on category
          element.classList.remove("hide");
        } else {
          //hide other elements
          element.classList.add("hide");
        }
      }
    });
}