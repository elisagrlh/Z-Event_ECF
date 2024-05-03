from django.shortcuts import render, redirect
from django.contrib. auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.models import User
#from django.conf import settings

from django.contrib.auth.hashers import make_password
from .forms import CreateUserForm
from .forms import AgeForm
from .forms import MultiSelectForm
from django.core.mail import send_mail
import secrets
import string
from mailjet_rest import Client
from django.http import HttpResponseForbidden
from .models import UserData
from .models import Live

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
#from django.shortcuts import get_object_or_404
from .utils import get_specific_live
from .utils import get_lives
from django.http import Http404



def index(request):
    return render(request, "business/index.html")

def adminLogin(request):
    #template_name = 'admin_login.html'
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.success(request, "there was an error loggin in, try again")
            return redirect("hidden_admin_login")
            
    else:
        return render(request, "business/adminlogin.html")

def loginForm(request):
    return render(request, "business/login-form.html")


class ConnexionView(TemplateView):
    template_name = "business/registration/login.html"


def login_user(request):
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirection vers la page d'accueil après la connexion réussie
                return redirect("index")
            else:
                # Retourner une erreur de connexion invalide
                messages.error(request, "Identifiants incorrects")
                return render(request, "business/streamerlogin.html", {'error': 'Identifiants incorrects'})
    else:
        return render(request, "business/streamerlogin.html")
    

def news(request):
    return render (request, "business/news.html")

def streamers(request):
    return render(request, "business/streamers.html")


def globalLives(request):
    lives = get_lives()
    #lives = Live.objects.select_related('streamer_name').all() # select_related est utilisé pour optimiser la requête
    #user = User.objects.all()
    return render(request, "business/global-lives.html", {"lives": lives})

def detailLive(request, id):
    live = get_specific_live(id)
    #user = User.objects.all()
    return render(request, 'business/detail-live.html', {'live': live})

def logout_user(request):
    logout(request)
    #messages.success(request, ("You were logged out"))
    return redirect("index")

@never_cache
def admindashboard(request):
    #User = settings.AUTH_USER_MODEL
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        ageForm = AgeForm(request.POST)
    
        if form.is_valid() and ageForm.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                messages.error(request, "Un compte avec cette adresse e-mail existe déjà.")
                return render(request, "business/admindashboard.html", {"form": form, "ageForm": ageForm})

            else:
                username=form.cleaned_data['username']

                new_user = form.save(commit=False)
                password = User.objects.make_random_password()
                new_user.set_password(password)
                new_user.save()

                # Création du profil associé avec l'âge
                user_data = ageForm.save(commit=False)
                user_data.user = new_user
                user_data.save()

                # Envoyer l'e-mail
                send_mail(
                    "Vos informations de connexion",
                    f"Votre nom d\'utilisateur est: {username}\nVotre mot de passe est: {password}\nVous pouvez vous connecter via: http://127.0.0.1:8000/login/",
                    "elisa.gerlach@efrei.net",  # Expéditeur
                    [email],  # Destinataire
                    fail_silently=False,
                )

                messages.success(request, "Utilisateur créé avec succès.")
 
    else:
        form = CreateUserForm()
        ageForm = AgeForm()
    
    if not request.user.is_superuser:
        return HttpResponseForbidden("Vous n'avez pas l'autorisation d'accéder à cette page.")
    else:
        return render(request, "business/admindashboard.html", {"form": form, "ageForm": ageForm, "users": User.objects.count()})

def count_users(request):
    user_count = User.objects.count()  # Compte tous les utilisateurs dans auth_user
    return render(request, 'count_users.html', {'user_count': user_count})

#@never_cache
def streamerdashboard(request, id):
    try:
        # Convertir id en int, cela lève une ValueError si ce n'est pas possible
        live_id = int(id)
    except ValueError:
        raise Http404("ID non valide")

    lives = get_lives()
    live = get_specific_live(live_id)

    if request.method == "POST":
        form = MultiSelectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")    
    else:
        form = MultiSelectForm()
        return render(request, "business/streamerdashboard.html", {"form": form, "lives": lives, "live": live})
    return render(request, "business/streamerdashboard.html", {"form": form, "lives": lives, "live": live})

'''
def some_view(request):
    user_profile = UserData.objects.get(user=request.user)
    login_count = user_profile.login_count
    # Maintenant, vous pouvez passer `login_count` à votre template
    return render(request, 'some_template.html', {'login_count': login_count})
'''

    