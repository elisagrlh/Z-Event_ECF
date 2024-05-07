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
            lives: [],
            selectedLive: {  // Initialisation de l'objet selectedLive
                label: '',
                streamer_pseudo: '',
                theme: '',
                start_date: '',
                end_date: '',
                pegi: '',
                material: []
            },
            editing: false,
            live_label: "[[ live.label ]]"

        }
    },
    mounted() {
        if (this.currentTab === 'HomeLives'){
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
            const assoPosition = this.$refs.asso.offsetTop;
            window.scrollTo({
            top: assoPosition,
            behavior: 'smooth'
            })
        },
        scrollToActus(){
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
        enableEditing(live) {
            live.editing = true; // Active le mode édition pour ce live
        },
        cancelEditing(live) {
            live.editing = false; // Active le mode édition pour ce live            // Optionnel: Recharger les données originales si nécessaire
        },
        updateLive(live) {
            console.log("Sending data to server:", { 
                label: live.label,
                streamer: live.streamer_pseudo,
                theme: live.theme,
                start_date: live.start_date,
                end_date: live.end_date,
                pegi: live.pegi,
                material : live.material,
                label : this.live_label
            });
            fetch(`/streamerdashboard/update/${live.id}/`, {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json',
                  'X-CSRFToken': '{{ csrf_token }}'
                },
                body: JSON.stringify({ 
                    label: live.label,
                    streamer_pseudo: live.streamer_pseudo,
                    theme: live.theme,
                    start_date: live.start_date,
                    end_date: live.end_date,
                    pegi: live.pegi,
                    material : live.material 
                })
              }).then(response => {
                if (!response.ok) throw new Error('Failed to update');
                return response.json();
              }).then(data => {
                this.editing = false;
                this.live_label = data.label;  // Mise à jour avec la nouvelle valeur confirmée
              }).catch(error => {
                console.error('Error:', error);
              });
        },

    }    
    })
    app.mount('#app')
