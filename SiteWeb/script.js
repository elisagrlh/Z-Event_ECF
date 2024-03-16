var openBtn = document.getElementById("openBtn");
var closeBtn = document.getElementById("closeBtn");
var hero = document.getElementById("hero");
var presentation = document.getElementById("presentation");


var homeBtn = document.getElementById("homeBtn");
var newsBtn = document.getElementById("newsBtn");


homeBtn.onclick = openHomePage;
newsBtn.onclick = openNewsPage;


function openHomePage()
{
    window.location.href = "index.html";
}


function openNewsPage()
{
    window.location.href = "news.html"
}