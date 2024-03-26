from django.urls import path

from . import views
#from .views import HiddenAdminLoginView
from django.views.generic import TemplateView
from .views import ConnexionView

#app_name = "business"
urlpatterns = [
    path("", views.index, name="index"),
    #path("connexion/", views.connexion, name="connexion"),
    #path('admin/login/', HiddenAdminLoginView.as_view(), name='hidden_admin_login'),
    path('login/', ConnexionView.as_view(), name='login'),
    path('admin/login/', views.adminLogin, name='hidden_admin_login'),
]