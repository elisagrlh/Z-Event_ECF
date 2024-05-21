from django.shortcuts import render, redirect
from django.contrib. auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.models import User
import json
#from django.conf import settings

from .forms import CreateUserForm, AddInfoForm, MultiSelectForm, LiveRegistrationForm
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from .models import Live, LiveRegistration, UserData


# Create your views here.
#from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from .utils import get_lives, get_specific_live, get_registration_lives, increment_click_stats, get_live_stats, format_changes

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LiveSerializer, LiveStatsSerializer, StreamerLivesSerializer
from django.http import JsonResponse
from django.db.models import Count, DateField
from django.db.models.functions import Trunc
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict




def index(request):
    return render(request, "business/index.html")

def adminLogin(request):
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


def login_user(request):
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user.is_staff=True
                print(user.is_staff)
                user.save()
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
    return render(request, "business/global-lives.html")


@api_view(['GET'])
def filterLives(request):
    lives = Live.objects.all()
    date = request.GET.get('date')
    theme = request.GET.get('theme')
    streamer = request.GET.get('streamer')
                
    if date:
       lives = lives.filter(start_date__date=date)
    if theme:
        lives = lives.filter(theme__name=theme)
    if streamer:
        lives = lives.filter(streamer_pseudo__pseudo=streamer)
        
    serializer = LiveSerializer(lives, many=True)
    return JsonResponse(serializer.data, safe=False)




@api_view(['GET',  "POST"])
def detailLive(request, id):
    live = get_specific_live(id)
    form = LiveRegistrationForm()

    if request.method == "POST":
        form = LiveRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            registration = form.save(commit=False)
            registration.live = live 
            registration.save()
            send_mail(
                    "Inscription Live",
                    f"Vous vous êtes inscrit.e au live {live.label}",
                    "elisa.gerlach@efrei.net",  # Expéditeur
                    [email],  # Destinataire
                    fail_silently=False,
                )
            return redirect("index")    
    return render(request, 'business/detail-live.html', {'live': live, "form": form})


def logout_user(request):
    logout(request)
    return redirect("index")

@never_cache
def admindashboard(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        addInfoForm = AddInfoForm(request.POST)
    
        if form.is_valid() and addInfoForm.is_valid():
            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                messages.error(request, "Un compte avec cette adresse e-mail existe déjà.")
                return render(request, "business/admindashboard.html", {"form": form, "addInfoForm": addInfoForm})

            else:
                username=form.cleaned_data['username']

                new_user = form.save(commit=False)
                password = User.objects.make_random_password()
                new_user.set_password(password)
                new_user.save()

                # Création du profil associé avec l'âge
                user_data = addInfoForm.save(commit=False)
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
                form = CreateUserForm()
                addInfoForm = AddInfoForm()
                messages.success(request, "Utilisateur créé avec succès.")
 
    else:
        form = CreateUserForm()
        addInfoForm = AddInfoForm()
    
    if not request.user.is_superuser:
        return HttpResponseForbidden("Vous n'avez pas l'autorisation d'accéder à cette page.")
    else:
        return render(request, "business/admindashboard.html", {"form": form, "addInfoForm": addInfoForm, "users": UserData.objects.count()})

def count_users(request):
    user_count = User.objects.count()  # Compte tous les utilisateurs dans auth_user
    return render(request, 'count_users.html', {'user_count': user_count})


@api_view(['GET'])
def streamerdashboard(request):
    lives = Live.objects.all()
    serializer = LiveSerializer(lives, many=True)
    return JsonResponse(serializer.data, safe=False)

def streamer_dashboard_page(request):
    lives = get_lives()
    if request.method == "POST":
        lives = get_lives()
        live_id = request.POST.get('live_id')
        if live_id:
            live = Live.objects.get(id=live_id)
            form = MultiSelectForm(request.POST, instance=live)
        else:
            form = MultiSelectForm(request.POST)

        if form.is_valid():
            original_data = model_to_dict(live) if live_id else {}
            updated_data = form.cleaned_data
            # Check for changes
            changes = {}
            for field in updated_data:
                if original_data.get(field) != updated_data[field]:
                    changes[field] = (original_data.get(field), updated_data[field])

            form.save()

            if changes and live_id:  # If there are any changes and it's an update
                # Retrieve all users who registered for this live
                registrations = LiveRegistration.objects.filter(live=live)
                emails = registrations.values_list('email', flat=True)
                
                # Format the changes for the email
                formatted_changes = format_changes(changes)
                # Send email to all registered users
                send_mail(
                    "Modification de Live",
                    f"Des modifications ont été apportées au live {live.label}. Voici les détails des changements:\n{formatted_changes}",
                    "elisa.gerlach@efrei.net",  # Expediteur
                    emails,  # Destinataires
                    fail_silently=False,
                )
            return redirect("index")    
    else:
        form = MultiSelectForm()
        live_id = request.GET.get('live_id')
        if live_id:
            live = Live.objects.get(id=live_id)
            form = MultiSelectForm(instance=live)
        #return render(request, "business/streamerdashboard.html", {"form": form})
    if not request.user.is_staff:
        return redirect("login_user")
    else:
        return render(request, "business/streamerdashboard.html", {"form": form, "lives": lives})
    return render(request, "business/streamerdashboard.html", {"form": form, "lives": lives})   


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

