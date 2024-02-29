var sidenav = document.getElementById("sideMenu");
var openBtn = document.getElementById("openBtn");
var closeBtn = document.getElementById("closeBtn");
var hero = document.getElementById("hero");
var presentation = document.getElementById("presentation");

const assoBtn = document.getElementById("assoButton");
const assoSection = document.getElementById("Assos");

const actusBtn = document.getElementById("actusBtn");
const actusSection = document.getElementById("Actus");


openBtn.onclick = openNav;
closeBtn.onclick = closeNav;
assoBtn.onclick = goToAssoSection;
actusBtn.onclick = goToAssoSection;

function openNav()
{
    sidenav.classList.add("active");
    //sidenav.style.display = 'block';
    hero.classList.add("activee");
    presentation.classList.add("activeee");
}

function closeNav()
{
    sidenav.classList.remove("active");
    //sidenav.style.display = 'none';
    hero.classList.remove("activee")
    presentation.classList.remove("activeee");
}

function goToAssoSection(target)
{
    if(target==="assoBtn")
    {
        assoSection.scrollIntoView({ behavior: 'smooth' }); 
    }

    if(target==="actusBtn")
    {
        actusSection.scrollIntoView({ behavior: 'smooth' });  
    }

}

assoBtn.addEventListener('click', function() {
    goToAssoSection("assoBtn");
});

actusBtn.addEventListener('click', function() {
    goToAssoSection("actusBtn");
});

/*assoBtn.addEventListener('click', function() {
    console.log("function go to asso");
    assoSection.scrollIntoView({ behavior: 'smooth' });
});*/
