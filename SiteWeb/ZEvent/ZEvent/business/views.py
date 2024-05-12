from django.shortcuts import render, redirect
from django.contrib. auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.models import User
import json
#from django.conf import settings

from .forms import CreateUserForm, AgeForm, MultiSelectForm, LiveRegistrationForm
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from .models import Live, LiveRegistration, UserData


# Create your views here.
#from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from .utils import get_lives, get_specific_live, get_registration_lives, increment_click_stats, get_live_stats

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LiveSerializer, LiveStatsSerializer, StreamerLivesSerializer
from django.http import JsonResponse
from django.db.models import Count, DateField
from django.db.models.functions import Trunc
from django.db.models import Prefetch


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
    return render(request, "business/global-lives.html", {"lives": lives})

def detailLive(request, id):
    live = get_specific_live(id)
    form = LiveRegistrationForm()
    #increment_click_stats(id)
    if request.method == "POST":
        form = LiveRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            registration = form.save(commit=False)
            registration.live = live 
            registration.save()
            send_mail(
                    "Inscription Live",
                    f"Vous vous êtes inscrit.e au live {live}",
                    "elisa.gerlach@efrei.net",  # Expéditeur
                    [email],  # Destinataire
                    fail_silently=False,
                )
            return redirect("index")    
        return render(request, 'business/detail-live.html', {'live': live, "form": form})
    return render(request, 'business/detail-live.html', {'live': live, "form": form})


def logout_user(request):
    logout(request)
    #messages.success(request, ("You were logged out"))
    return redirect("index")

@never_cache
def admindashboard(request):
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
@api_view(['GET'])
def streamerdashboard(request):
    if request.method == 'GET':
        lives = get_lives()
        registrations = get_registration_lives()
        
        live_reg_data = []
        serializer = LiveSerializer(lives, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def registration_live(request):
    live_reg_data = (
        LiveRegistration.objects
        .annotate(date=Trunc('live__start_date', 'day', output_field=DateField()))
        .values('date')
        .annotate(user_count=Count('id'))
        .order_by('date')
    )
    data = [
        {'date': reg['date'].strftime('%Y-%m-%d'), 'user_count': reg['user_count']}
        for reg in live_reg_data
    ]
    return JsonResponse({'data': data})


def streamer_dashboard_page(request):
    if request.method == "POST":
        live_id = request.POST.get('live_id')
        if live_id:
            live = Live.objects.get(id=live_id)
            form = MultiSelectForm(request.POST, instance=live)
        else:
            form = MultiSelectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")    
    else:
        form = MultiSelectForm()
        live_id = request.GET.get('live_id')
        if live_id:
            live = Live.objects.get(id=live_id)
            form = MultiSelectForm(instance=live)
        #return render(request, "business/streamerdashboard.html", {"form": form})
    return render(request, "business/streamerdashboard.html", {"form": form})


def increment_click(request, id):
    increment_click_stats(id)
    return redirect("detailLive", id=id)   

@api_view(['GET'])
def stats(request):
    livestats = get_live_stats()
    serializer = LiveStatsSerializer(livestats, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def streamer_lives_view(request):
    users_with_lives = UserData.objects.all()
    serializer = StreamerLivesSerializer(users_with_lives, many=True)
    return Response(serializer.data)