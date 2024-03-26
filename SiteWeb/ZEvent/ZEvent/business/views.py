from django.shortcuts import render

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
    f = open("C:/xampp/htdocs/ECF/SiteWeb/ZEvent/ZEvent/business/templates/business/adminlogin.html", "r")
    resp = f.read()
    return HttpResponse(f"{resp}")


class ConnexionView(TemplateView):
    template_name = 'business/login.html'