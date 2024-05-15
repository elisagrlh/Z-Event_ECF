
let app = Vue.createApp({
    delimiters: ['[[', ']]'],
    //name: 'ChartComponent',
    data: function(){
        return{
            hasNewClassMenu: false,
            hasNewClassPresentation: false,
            currentTab: "FirstTab",
            showDropdown: false,
            lives: [],
            themes: [],
            theme:'',
            date:'',
            streamer:'',
            //streamers: [],
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
            livestats: [],
            filter_lives: [],
            streamers: [],
            chart: null,

        }
    },
    mounted() {
        this.fetchLives();
        this.fetchLiveStats();
        this.fetchLiveStreamers();
        //this.filterLives();
    },
    watch: {
        currentTab(newVal) {
          if (newVal === 'UserRegistration') {
            this.$nextTick().then(() => {
              this.fetchLivesReg();
            });
          }
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
                    this.themes = [...new Set(data.flatMap(live => live.theme.map(t => t.name)))];  // Unique themes
                    this.streamers = [...new Set(data.map(live => live.streamer_pseudo))];  // Unique streamers
 
                })
                .catch(err => console.error(err));
           
        },


        filterLives(){
            console.log("filterLives called");
            let params = new URLSearchParams({
                date: this.date,
                theme: this.theme,
                streamer: this.streamer
            });
            console.log("streamer", this.streamer)
            if (this.theme) {
                params.set('theme', this.theme.toString());
            }
            console.log(params.toString());  // Inspecter les paramètres
            console.log("URL with parameters:", `/api/filterlives/?${params.toString()}`);   
            
            fetch(`/api/filterlives/?${params.toString()}`)
                .then(response => response.json())
                .then(data => {
                    console.log("Data received from API:", data);
                    this.lives = data;
                    
                    this.themes = [...new Set(data.flatMap(live => live.theme.map(t => t.name)))];  // Unique themes
                    this.streamers = [...new Set(data.map(live => live.streamer_pseudo))];  // Unique streamers
 
                })
                .catch(err => console.error(err));
        },

        clearFilters() {
            this.date = '';
            this.theme = '';
            this.streamer = '';
            this.fetchLives();  // Recharger les données initiales
        },


        fetchLiveStats() {
            // Faire une requête pour récupérer les données
            fetch('/api/stats/') 
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data && data.length > 0) { // Vérifie que data est non nul et non vide
                    this.livestats = data; // Stockage des données dans la propriété livestats
                } else {
                    console.log('No live stats data received');
                }
            })
            .catch(error => {
                console.error('There has been a problem with your fetch operation:', error);
            });
        },


        fetchLiveStreamers(){
            fetch('/api/streamers/')
            .then(response => response.json())
            .then(data => {
                this.streamers = data;
            })
            .catch(err => console.error(err));

        },

        fetchLivesReg() {
            fetch('/api/registration/')
                .then(response => response.json())
                .then(data => {
                    this.displayChart(data);
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
            this.isEditMode = false; // Désactive le mode édition pour ce live 

            document.getElementById('id_label').value = null;
            document.getElementById('id_streamer_pseudo').value = null;
            document.getElementById('id_start_date').value = null;
            document.getElementById('id_end_date').value = null; 
            document.getElementById('id_theme').value = null;
            document.getElementById('id_pegi').value = null;
            document.getElementById('id_material').value = null;
            this.uncheckCheckboxes();
        },

        displayChart(data) {
            this.$nextTick(() => {
              const ctx = document.getElementById('myChart');
              if (ctx && !this.chart) {
                const dates = data.data.map(item => item.date);   // Extraction des dates
                const userCounts = data.data.map(item => item.user_count);  // Extraction des comptes d'utilisateurs
                this.initializeChart(ctx, dates, userCounts);
              }
            });
          },

        initializeChart(ctx, dates, userCounts) { 
            if (this.chart) {
              this.chart.destroy();
            }

            const maxValue = Math.max(...userCounts);
            let stepSize;
            if (maxValue <= 10) {
                stepSize = 1;
            } else if (maxValue <= 100) {
                stepSize = 10;
            } else {
                stepSize = 100;
            }

            this.chart = new Chart(ctx.getContext('2d'), {
              type: 'bar',
              data: {
                labels: dates,
                datasets: [{
                  label: "Nombres d'inscriptions",
                  data: userCounts,
                  //borderWidth: 1,
                  //fill: false
                }]
              },
              options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            // Ajuster stepSize selon les besoins
                            stepSize: stepSize
                        }
                    }
                }

              }
              
            });
        },

        calculateMaterials(lives) {
            let allMaterials = [];
            let materialsToBuy = [];
          
            // Collecter tous les matériels de tous les lives
            lives.forEach(live => {
              live.material.forEach(material => {
                allMaterials.push({
                  label: material.label,
                  brand: material.brand,
                  start_date: new Date(live.start_date),
                  end_date: new Date(live.end_date)
                });
              });
            });
          
            // Traitement des matériels pour déterminer le nombre nécessaire
            allMaterials.forEach(current => {
              let overlaps = 0;
          
              allMaterials.forEach(other => {
                if (current.label === other.label && current.brand === other.brand) {
                  if (!(current.end_date <= other.start_date || current.start_date >= other.end_date)) {
                    overlaps++;
                  }
                }
              });
          
              let existingCount = materialsToBuy.filter(m => m.label === current.label && m.brand === current.brand).length;
          
              if (existingCount < overlaps) {
                for (let i = existingCount; i < overlaps; i++) {
                  materialsToBuy.push({
                    label: current.label,
                    brand: current.brand
                  });
                }
              }
            });
          
            return materialsToBuy;
          }

    }    
    })
    app.mount('#app')
