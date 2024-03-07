var sidenav = document.getElementById("sideMenu");
var openBtn = document.getElementById("openBtn");
var closeBtn = document.getElementById("closeBtn");
var hero = document.getElementById("hero");
var presentation = document.getElementById("presentation");

const assoBtn = document.getElementById("assoButton");
const assoSection = document.getElementById("Assos");

const actusBtn = document.getElementById("actusBtn");
const actusSection = document.getElementById("Actus");

var connexionBtn = document.getElementById("connexionBtn");
var homeBtn = document.getElementById("homeBtn");
var newsBtn = document.getElementById("newsBtn");

openBtn.onclick = openNav;
closeBtn.onclick = closeNav;
assoBtn.onclick = goToAssoSection;
actusBtn.onclick = goToAssoSection;
connexionBtn.onclick = openConnexionPage;
homeBtn.onclick = openHomePage;
newsBtn.onclick = openNewsPage;


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


function openConnexionPage()
{
    window.location.href = "connexion.html";
}

function openHomePage()
{
    window.location.href = "index.html";
}


function openNewsPage()
{
    window.location.href = "news.html"
}