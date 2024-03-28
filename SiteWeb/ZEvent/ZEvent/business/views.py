from django.shortcuts import render, redirect
from django.contrib. auth import authenticate, login, logout
from django.contrib import messages 

# Create your views here.
from django.http import HttpResponse
from django.template import loader
#from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView



def index(request):
    #f = open("C:/xampp/htdocs/ECF/SiteWeb/ZEvent/ZEvent/business/templates/business/index.html", "r")
    #resp = f.read()
    #template = loader.get_template("business/index.html")
    #return HttpResponse(f"{resp}")
    #return HttpResponse(template.render(request=request))
    return render(request, "business/index.html")

#def connexion(request):
    #f = open("C:/xampp/htdocs/ECF/SiteWeb/ZEvent/ZEvent/business/templates/business/connexion.html", "r")
    #resp = f.read()
    #return HttpResponse(f"{resp}")
    #return render(request, "business/connexion.html")

#class HiddenAdminLoginView(LoginView):
def adminLogin(request):
    #template_name = 'admin_login.html'
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "there was an error loggin in, try again")
            return redirect("hidden_admin_login")
            
    else:
        return render(request, 'business/adminlogin.html')

def loginForm(request):
    return render(request, "business/login-form.html")


class ConnexionView(TemplateView):
    template_name = 'business/registration/login.html'


def login_user(request):
    return render (request, "business/login1.html")

def news(request):
    return render (request, 'business/news.html')

def streamers(request):
    return render(request, 'business/streamers.html')