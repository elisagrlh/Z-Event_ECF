# Z-Event_ECF - Elisa Gerlach

Ce projet est une application web Django utilisant une base de données PostgreSQL. Il est conçu pour vous aider à démarrer rapidement avec Django et PostgreSQL.

## Prérequis

Avant de commencer, assurez vous d'avoir installé les éléments suivants sur votre système :

-   Python (version 3.x recommandée)
-   PostgreSQL
-   Pip (gestionnaire de paquets Python)

## Environnement virtuel (venv)

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de ce projet et éviter les conflits avec d'autres projets Python sur votre système.

1.  Créez un environnement virtuel en utilisant Python venv. Exécutez la commande suivante dans le répertoire racine du projet :

```bash/powershell
python -m venv venv
```

Cela créera un répertoire `venv` dans votre répertoire de projet, contenant l'environnement virtuel.

2.  Activez l'environnement virtuel. Selon votre système d'exploitation, la commande pour activer l'environnement virtuel peut varier :

-   Sur Windows :

```PowerShell
venv\Scripts\activate
``` 

-   Sur MacOs et Linux :

```bash
source venv/bin/activate
``` 

Une fois l'environnement virtuel activé, vous verrez `(venv)` préfixé à votre invite de commande.

3.  Installez les dépendances requises à l'intérieur de l'environnement virtuel en exécutant :

```bash/powershell
pip install -r requirements.txt
```

## Installation

1.  Clonez ce dépôt sur votre machine locale :

```bash/powershell
git clone https://github.com/elisagrlh/Z-Event_ECF
```

2.  Accédez au répertoire du projet :

```bash/powershell
cd Z-Event_ECF
``` 

3.  Installez les dépendances requises à l'aide de pip :

```bash/powershell
pip install -r requirements.txt
``` 

le fichier requirement.txt se situe au même niveau que le dossier venv. 




## Configuration du service PostgreSQL

Si vous utilisez PostgreSQL en tant que service, assurez vous que le service est en cours d'exécution et que vous avez les informations de connexion nécessaires.

1.  Assurez vous que le service PostgreSQL est en cours d'exécution sur votre système. Vous pouvez l'installer à partir de ce lien : https://www.postgresql.org/download/
Sous Linux :
```bash
apt get install postgresql
```
```bash
systemctl enable postgresql.service --now
systemctl enable postgresql.service
```
```SQL
CREATE USER user WITH PASSWORD 'password';
CREATE DATABASE dbname;
GRANT ALL PRIVILEGES ON DATABASE dbname OWNER TO user;
ALTER DATABASE dbname OWNER user;
```
Il est possible qu'une erreur de version de collocation soit générée, dans ce cas faire la commande suivante puis refaire les commandes ayant échouées :
```SQL
ALTER DATABASE template1 REFRESH COLLOCATION VERSION;
```
2.  Obtenez les informations de connexion nécessaires, telles que le nom d'utilisateur, le mot de passe, l'hôte et le port du service.

Assurez vous de mettre à jour les paramètres de la base de données dans le fichier `.env` avec les informations de connexion appropriées.



## Configuration des variables d'environnement

Ce projet utilise un fichier `.env` pour stocker les informations sensibles et les paramètres de configuration. Le fichier `.env` est un moyen pratique de garder ces informations hors du code source et de les charger dynamiquement lors de l'exécution du projet.

1.  Créez un fichier nommé `.env` dans le répertoire racine du projet s'il n'existe pas déjà et ajoutez les variables d'environnement suivantes au fichier `.env`, en remplaçant les valeurs par les vôtres :

```
DB_NAME= "your_db_name_here",
DB_USER= "your_db_user_here",
DB_PASSWORD= "your_db_password_here",
```
2. Ajoutez également au .env les credentials pour Mailjet :
```
API_KEY='0c40e0aebb2641bbe37c8a4e82805c1b'
SECRET_KEY_API='eebe476df7603af61fe60dff5395f392'
SMTP_HOST='in-v3.mailjet.com'
SMTP_PORT=587
SMTP_USER='0c40e0aebb2641bbe37c8a4e82805c1b'
SMTP_PASSWORD='eebe476df7603af61fe60dff5395f392'
```

3. Générez une SECRET_KEY aléatoire à mettre dans les settings.py :
```hash/powershell
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

4. Ajouter cette clef dans settings.py :
```python
SECRET_KEY='clef_générée'
```
## Configuration de la base de données

1.  Connectez vous à votre instance PostgreSQL.
    
2.  Créez une nouvelle base de données pour le projet :
   
Dans settings.py:

```python
import os
from dotenv import load_dotenv
load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
``` 

Dans .my_pgpass:

```
127.0.0.1:5432:your_db_name_here:your_db_user_here:your_db_password_here
```

Remplacez `'your_db_name_here'`, `'your_db_user_here'` et `'your_db_password_here'` par les informations appropriées.

### Configuration de .pg_service.conf

C'est  une étape optionnelle mais pour simplifier la gestion des connexions PostgreSQL, vous pouvez utiliser un fichier de configuration `.pg_service.conf`. Ce fichier vous permet de spécifier les paramètres de connexion pour différents services PostgreSQL.

1.  Créez ou éditez le fichier `.pg_service.conf`. Par défaut, ce fichier est généralement situé dans le répertoire principal de votre utilisateur (`~/.pg_service.conf` sur macOS et Linux, `%APPDATA%\local\pgadmin4\UserData\pg_service.conf` sur Windows).
    
2.  Ajoutez une entrée pour votre service PostgreSQL en spécifiant le nom du service, l'hôte, la base de données, le nom d'utilisateur et éventuellement le port. Voici un exemple :

```txt
[my_service]
host=127.0.0.1
user=USER
dbname=NAME
port=5432
```

## Configuration du service Mongodb Atlas

1. Il vous faudra créer un compte Mongodb Atlas.

Si vous souhaitez utiliser votre propre base de données :
1. Créez une organisation, un projet et une base de données
2. Ajoutez vos credentials dans settings.py

Si vous souhaitez utiliser ma base de données :
1. Utilisez les credentials suivants dans settings.py (n'hésitez pas à remplacer par des variables d'environnement) :  
Pour la version locale :
```python
DATABASES = {
    "default":{
            #informations base de données par défaut
        },
    'mongodb': {
        'ENGINE': 'djongo',
                'NAME': 'Zeventdb',
                'ENFORCE_SCHEMA': False,
                'CLIENT': {
                    'host': 'mongodb+srv://elisa:user123@zevent0.b4gz6jb.mongodb.net/?retryWrites=true&w=majority&appName=ZEvent0'
                } 
        }
}
```

Pour la version déployée :
```python
DATABASES = {
    "default":{
            #informations base de données par défaut
        },
    'mongodb': {
        'ENGINE': 'djongo',
                'NAME': 'Zeventdbdeploy',
                'ENFORCE_SCHEMA': False,
                'CLIENT': {
                    'host': 'mongodb+srv://elisa:user123@zevent0.b4gz6jb.mongodb.net/?retryWrites=true&w=majority&appName=ZEvent0'
                } 
        }
}
```

Si vous souhaitez simplement visualiser ma base de données existante, voici une clef API qui vous permettra de print la base de données :
```
public: tnlaroch
privée: 619b8dff-e465-48a2-b868-113744d5ba8f
```

Si vous souhaitez avoir accès directement à ma base de données depuis l'interface Atlas sur un navigateur vous pouvez m'envoyer un mail à l'adresse elisagerlach17@gmail.com de manière à ce que j'ai connaissance de votre adresse mail et que je puisse vous ajouter dans Atlas (une adresse mail est obligatoire dans ce cas de figure). Je m'engage à vous répondre dans les plus brefs délais.



## Création d'un superutilisateur Django

Après avoir configuré la base de données, vous pouvez créer un superutilisateur Django pour accéder à l'interface d'administration et effectuer des opérations administratives.

1. Créez d'abord les tables dans la base de données  avec la commande suivante :

```bash/powershell
python manage.py migrate
```

1.  Exécutez la commande suivante :

```bash/powershell
python manage.py createsuperuser
``` 

2.  Suivez les instructions à l'écran pour fournir un nom d'utilisateur, une adresse e-mail et un mot de passe pour le superutilisateur.

Une fois que vous avez créé le superutilisateur, vous pouvez accéder à l'interface d'administration en démarrant le serveur de développement et en visitant `http://127.0.0.1:8000/admin/`.

Si vous avez des questions ou des difficultés, n'hésitez pas à demander de l'aide dans les issues du dépôt.

## Lancement du serveur de développement

1.  Lancez le serveur de développement :


```bash/powershell
python manage.py runserver
``` 

Le serveur devrait démarrer sur `http://127.0.0.1:8000/`.


## Auteurs

elisagerlach17@gmail.com
