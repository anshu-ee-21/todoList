const toggleBtn = document.getElementById('toggle');
console.log('Hello');
const links = document.getElementsByClassName('nav-link');
toggleBtn.addEventListener("click", function(){
    for(var i=0; i<links.length;i++){
        links[i].classList.toggle('active');
    }
})