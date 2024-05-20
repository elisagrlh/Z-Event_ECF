# Z-Event_ECF -Elisa Gerlach

Ce projet est une application web Django utilisant une base de données PostgreSQL. Il est conçu pour vous aider à démarrer rapidement avec Django et PostgreSQL.

## Prérequis

Avant de commencer, assurez vous d'avoir installé les éléments suivants sur votre système :

-   Python (version 3.x recommandée)
-   PostgreSQL
-   Pip (gestionnaire de paquets Python)

## Installation

1.  Clonez ce dépôt sur votre machine locale :

`git clone https://github.com/elisagrlh/Z-Event_ECF` 

2.  Accédez au répertoire du projet :

`cd Z-Event_ECF` 

3.  Installez les dépendances requises à l'aide de pip :

`pip install -r requirements.txt` 

## Environnement virtuel (venv)

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de ce projet et éviter les conflits avec d'autres projets Python sur votre système.

1.  Créez un environnement virtuel en utilisant Python venv. Exécutez la commande suivante dans le répertoire racine du projet :

`python -m venv venv` 

Cela créera un répertoire `venv` dans votre répertoire de projet, contenant l'environnement virtuel.

2.  Activez l'environnement virtuel. Selon votre système d'exploitation, la commande pour activer l'environnement virtuel peut varier :

-   Sur Windows :

`venv\Scripts\activate` 

-   Sur MacOs et Linux :

`source venv/bin/activate` 

Une fois l'environnement virtuel activé, vous verrez `(venv)` préfixé à votre invite de commande.

3.  Installez les dépendances requises à l'intérieur de l'environnement virtuel en exécutant :

`pip install -r requirements.txt`

## Configuration des variables d'environnement

Ce projet utilise un fichier `.env` pour stocker les informations sensibles et les paramètres de configuration. Le fichier `.env` est un moyen pratique de garder ces informations hors du code source et de les charger dynamiquement lors de l'exécution du projet.

1.  Créez un fichier nommé `.env` dans le répertoire racine du projet, s'il n'existe pas déjà.
    
2.  Ajoutez les variables d'environnement suivantes au fichier `.env`, en remplaçant les valeurs par les vôtres :

`API_KEY='0c40e0aebb2641bbe37c8a4e82805c1b'
SECRET_KEY_API='eebe476df7603af61fe60dff5395f392'
SMTP_HOST='in-v3.mailjet.com'
SMTP_PORT=587
SMTP_USER='0c40e0aebb2641bbe37c8a4e82805c1b'
SMTP_PASSWORD='eebe476df7603af61fe60dff5395f392'`

## Configuration du service PostgreSQL

Si vous utilisez PostgreSQL en tant que service, assurez vous que le service est en cours d'exécution et que vous avez les informations de connexion nécessaires.

1.  Assurez vous que le service PostgreSQL est en cours d'exécution sur votre système.
2.  Obtenez les informations de connexion nécessaires, telles que le nom d'utilisateur, le mot de passe, l'hôte et le port du service.

Assurez vous de mettre à jour les paramètres de la base de données dans le fichier `.env` avec les informations de connexion appropriées.

### Configuration de .pg_service.conf

C'est  une étape optionnelle mais pour simplifier la gestion des connexions PostgreSQL, vous pouvez utiliser un fichier de configuration `.pg_service.conf`. Ce fichier vous permet de spécifier les paramètres de connexion pour différents services PostgreSQL.

1.  Créez ou éditez le fichier `.pg_service.conf`. Par défaut, ce fichier est généralement situé dans le répertoire principal de votre utilisateur (`~/.pg_service.conf` sur macOS et Linux, `%APPDATA%\local\pgadmin4\UserData\pg_service.conf` sur Windows).
    
2.  Ajoutez une entrée pour votre service PostgreSQL en spécifiant le nom du service, l'hôte, la base de données, le nom d'utilisateur et éventuellement le port. Voici un exemple :

[my_service]
host=localhost
user=USER
dbname=NAME
port=5432

## Configuration de la base de données

1.  Connectez vous à votre instance PostgreSQL.
    
2.  Créez une nouvelle base de données pour le projet :
   
Dans settings.py:

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_votre_base_de_donnees',
        'USER': 'votre_utilisateur',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}` 

Dans .my_pgpass:

`localhost:5432:nom_de_votre_base_de_donnees:votre_utilisateur:votre_mot_de_passe`

Remplacez `'nom_de_votre_base_de_donnees'`, `'votre_utilisateur'` et `'votre_mot_de_passe'` par les informations appropriées. Si vous avez utilisé un .env

## Création d'un superutilisateur Django

Après avoir configuré la base de données, vous pouvez créer un superutilisateur Django pour accéder à l'interface d'administration et effectuer des opérations administratives.

1.  Dans votre terminal, exécutez la commande suivante :

`python manage.py createsuperuser` 

2.  Suivez les instructions à l'écran pour fournir un nom d'utilisateur, une adresse e-mail et un mot de passe pour le superutilisateur.

Une fois que vous avez créé le superutilisateur, vous pouvez accéder à l'interface d'administration en démarrant le serveur de développement et en visitant `http://127.0.0.1:8000/admin/`.

Si vous avez des questions ou des difficultés, n'hésitez pas à demander de l'aide dans les issues du dépôt.

## Lancement du serveur de développement

1.  Effectuez les migrations initiales pour créer les tables de base de données :

`python manage.py migrate` 

3.  Lancez le serveur de développement :


`python manage.py runserver` 

Le serveur devrait démarrer sur `http://127.0.0.1:8000/`.


## Auteurs

elisagerlach17@gmail.com
