
main();

function main(){

    for(let i = 1; i < 5; i++){
        document.querySelectorAll(".bubble")[i].style.width = "16%";
    }
}


function expander(thisbutton){
    var parentWidth = document.querySelector("."+thisbutton).parentElement.parentElement.style.width;
    // console.log(thisbutton)
    // console.log(parentWidth) 

        if(document.querySelector("."+thisbutton).parentElement.parentElement.style.width == '98%'){
            document.querySelector("."+thisbutton).parentElement.parentElement.style.width = '16%';
            console.log("attempt to change width to 16%");
            document.querySelector("."+thisbutton).nextElementSibling.style.opacity = "0%";
            document.querySelector("."+thisbutton).previousElementSibling.style.opacity = "100%";
            
            document.querySelector("."+thisbutton).innerHTML = "+"; //change button to +

        }else{
            document.querySelector("."+thisbutton).parentElement.parentElement.style.width = '98%';
            console.log("attempt to change width to 98%");
            
            setTimeout(() => {
                document.querySelector("."+thisbutton).nextElementSibling.style.opacity = "100%";
                document.querySelector("."+thisbutton).previousElementSibling.style.opacity = "0%";
            }, "750")

            document.querySelector("."+thisbutton).innerHTML = "-"; //change button to -

            if(document.querySelector("."+thisbutton).parentElement.classList.contains("education") === true ){
                let mySkills = document.getElementById("mySkills");
                skills.forEach((skill) => {
                    let li = document.createElement("li");
                    li.innerHTML = skill;
                    mySkills.appendChild(li);
                })    
            };
        }
    
    console.log(parentWidth);
}


// needed to make smooth scroll effect work on all browsers
$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();
  
    $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top
    }, 1000);
});


const skills = [
    "Software development and programming skills in languages such as Python, C, Python, JavaScript, and HTML/CSS.",
    "Proficiency in network design and implementation, including LAN, WAN, and wireless networks.",
    "Knowledge of database design, administration, and maintenance.",
    "Experience with microcontroller programming, hardware interfacing, and embedded systems design.",
    "Understanding of computer architecture, operating systems, and computer hardware components.",
    "Familiarity with software development methodologies and tools, such as Git.",
    "Strong analytical and problem-solving skills to identify and troubleshoot complex issues.",
    "Ability to design and develop IoT solutions using sensors, actuators, and other devices.",
    "Strong mathematical skills, including algebra, calculus, and statistics.",
    "Knowledge of cybersecurity and data privacy principles to secure computer systems and networks.",
    "Good communication skills to collaborate with cross-functional teams and stakeholders.",
    "Ability to document technical designs, requirements, and project specifications.",
    "Experience with project management methodologies and tools to manage project timelines and budgets.",
    "Fundamental understanding of machine learning, artificial intelligence, and data analytics principles to analyze and interpret data.",
    "Familiarity with cloud computing, virtualization, and containerization technologies."
  ];
  
