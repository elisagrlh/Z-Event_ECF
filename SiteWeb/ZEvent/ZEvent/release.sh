#!/bin/bash

# Sortir en cas d'erreur
set -e

# Naviguer au répertoire du projet si nécessaire
#cd C:/xampp/htdocs/ECF/SiteWeb/ZEvent/ZEvent

# Activer l'environnement virtuel
#source venv/Scripts/activate

# Exécuter les migrations
python manage.py migrate --noinput

# Créer un utilisateur administrateur
python manage.py create_admin

# Remplir la table OptionsMaterial
python manage.py fill_options_material

#Remplir la table OptionsTheme
python manage.py fill_options_theme
