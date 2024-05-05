/*var openBtn = document.getElementById("openBtn");
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
}*/




            

let app = Vue.createApp({
    delimiters: ['[[', ']]'],
    data: function(){
        return{
            hasNewClassMenu: false,
            hasNewClassPresentation: false,
            currentTab: "FirstTab",
            showDropdown: false,

            lives: []

        }
    },

    mounted() {
        if (this.currentTab === 'HomeLives')
        {
            this.fetchLives();
        }
    },
    methods: {
        openBtn() {
        this.hasNewClassMenu = true;
        this.hasNewClassPresentation = true;
        },
                
        closeBtn(){
            this.hasNewClassMenu = false;
            this.hasNewClassPresentation = false;

        },

        scrollToAsso(){
            //const assoElement = getElementById("Assos");
            const assoPosition = this.$refs.asso.offsetTop;
            window.scrollTo({
            top: assoPosition,
            behavior: 'smooth'
            })
        },

        scrollToActus(){
            //const assoElement = getElementById("Assos");
            const actusPosition = this.$refs.actus.offsetTop;
            window.scrollTo({
            top: actusPosition,
            behavior: 'smooth'
            })
        },

        redirectWWF(){
            window.open("https://www.wwf.fr/", "_blank");
        },


        closeDropdown(dropdown) {
            this.dropdowns[dropdown] = false;
        },
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },

        changeTab(tabName) {
            console.log("Changing tab to:", tabName);
            this.currentTab = tabName;
            if (tabName === 'HomeLives') {
                this.fetchLives();
            }
        },
        fetchLives() {
            console.log("Fetching lives data...");
            fetch('/api/streamerdashboard/')
                .then(response => response.json())
                .then(data => {
                    this.lives = data;
                })
                .catch(err => console.error(err));
        },
        

    }    
    })
    app.mount('#app')
