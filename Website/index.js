
main();

function main(){

    for(let i = 0; i < 4; i++){
        document.querySelectorAll(".bubble")[i].style.width = "18%";
    }
}



function expander(thisbutton){
    var parentWidth = document.querySelector("."+thisbutton).parentElement.parentElement.style.width;
    // console.log(thisbutton)
    // console.log(parentWidth) 

    if(document.querySelector("."+thisbutton).parentElement.parentElement.style.width == '98%'){
        document.querySelector("."+thisbutton).parentElement.parentElement.style.width = '18%';
        console.log("attempt to change width to 18%");
        console.log(document.querySelector("."+thisbutton).nextElementSibling.classList.add('hidden'));
    }else{
        document.querySelector("."+thisbutton).parentElement.parentElement.style.width = '98%';
        console.log("attempt to change width to 98%");
        console.log(document.querySelector("."+thisbutton).nextElementSibling.classList.remove('hidden'));
    }
    
    console.log(parentWidth);
}


// blob stuff
