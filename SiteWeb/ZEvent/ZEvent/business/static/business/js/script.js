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
            live_label: "[[ live.label ]]",
            isEditMode: false,
            live: {},

        }
    },
    mounted() {
        this.fetchLives();
        
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
            this.currentTab = tabName;
            if (tabName === 'HomeLives') {
                this.fetchLives();
            }
        },
        fetchLives() {
            fetch('/api/streamerdashboard/')
                .then(response => response.json())
                .then(data => {
                    this.lives = data;
                })
                .catch(err => console.error(err));
        },
    


        changeOptionByText(selectId, searchText) {
            var select = document.getElementById(selectId);
            for (var i = 0; i < select.options.length; i++) {
                if (select.options[i].text === searchText) {
                    document.getElementById('id_streamer_pseudo').value=select.options[i].value;
                    return select.options[i]; // Return the matching option element
                }
            }
            return null; // Return null if no matching option was found
        },

        checkThemesCheckbox()
        {
            var themeLabels = document.querySelectorAll('#id_theme div > label');
                themeLabels.forEach(function(label) {
                    theme_labels = label.textContent.trim();
                    for (var i = 0; i < document.getElementById('id_theme').value.length; i++) {
                        var checkboxId = label.getAttribute('for');
                        var checkbox = document.getElementById(checkboxId);
                        if (theme_labels === document.getElementById('id_theme').value[i].name)
                        {
                            checkbox.checked = true;
                        }
                    }
                });
        },
        checkMaterialCheckbox()
        {
            var matLabels = document.querySelectorAll('#id_material div > label');
            matLabels.forEach(function(label) {
                mat_labels = label.textContent.trim();
                for (var i = 0; i < document.getElementById('id_material').value.length; i++) {
                    var checkboxId = label.getAttribute('for');
                    var checkbox = document.getElementById(checkboxId);
                    var labels = document.getElementById('id_material').value[i].label;
                    var brand = document.getElementById('id_material').value[i].brand;
                    var fullLabel = labels + " (" + brand + ")"; // Concaténation du label et de la marque
                    if (mat_labels === fullLabel) {
                        checkbox.checked = true;
                    }
                }
            });
        },

        uncheckCheckboxes(){
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
                checkboxes.forEach(function(checkbox) {
                    checkbox.checked = false;
                });
        },


        enableEditing(live) {
            this.live = {...live};
            this.isEditMode = true;
            this.selectedLive = live;
            console.log(live.id);
            this.currentTab = 'FirstTab';  // Change l'onglet
            this.$nextTick(() => { // Attend que VueJS ait fini de mettre à jour le DOM
                document.getElementById('id_label').value = this.selectedLive.label;
                document.getElementById('id_streamer_pseudo').value = this.selectedLive.streamer_pseudo;
                document.getElementById('id_start_date').value = live.start_date.slice(0, 16);
                document.getElementById('id_end_date').value = live.end_date.slice(0, 16); 
                document.getElementById('id_theme').value = live.theme;
                document.getElementById('id_pegi').value = live.pegi;
                document.getElementById('id_material').value = live.material;

                this.changeOptionByText('id_streamer_pseudo', this.selectedLive.streamer_pseudo);
                this.checkThemesCheckbox();
                this.checkMaterialCheckbox();
            });
                                                                                                                                                                                                                                        
        },


        cancelEditing() {
            this.isEditMode = false; // Active le mode édition pour ce live 

            document.getElementById('id_label').value = null;
            document.getElementById('id_streamer_pseudo').value = null;
            document.getElementById('id_start_date').value = null;
            document.getElementById('id_end_date').value = null; 
            document.getElementById('id_theme').value = null;
            document.getElementById('id_pegi').value = null;
            document.getElementById('id_material').value = null;
            this.uncheckCheckboxes();
        },

    }    
    })
    app.mount('#app')
