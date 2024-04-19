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
    data: function(){
        return{
            hasNewClassMenu: false,
            hasNewClassPresentation: false,
            emailInput: '',
            passwordInput: '',
            currentTab: 'streamerCreation',
            selectedStartDate: '',
            selectedStartTime: '',
            selectedEndDate: '',
            selectedEndTime: '',

            showDropdown: false,
            options: [
            { id: 'monitor', text: 'Moniteur', value: 'monitor' },
            { id: 'mouse', text: 'Souris', value: 'mouse' },
            { id: 'keyboard', text: 'Clavier', value: 'keyboard' }
            ],
            selectedOptions: []
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

        /*toggleDropdown(dropdown) {
            this.dropdowns[dropdown] = !this.dropdowns[dropdown];
        },*/

        closeDropdown(dropdown) {
            this.dropdowns[dropdown] = false;
        },
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },
    }    
    })
    app.mount('#app')
