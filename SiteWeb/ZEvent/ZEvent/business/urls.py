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
    path('login1/', ConnexionView.as_view(), name='login'),
    path('adminlogin/', views.adminLogin, name='hidden_admin_login'),

    path('login/', views.login_user, name="login_user"),

    path('news/', views.news, name='news'),
    path('streamers/', views.streamers, name='streamers'),
    path('api/streamers/', views.streamer_lives_view, name='streamers-api'),

    path("admindashboard/", views.admindashboard, name="admindashboard"),
    path("streamerdashboard/", views.streamer_dashboard_page, name="streamerdashboard"),
    path("globalLives/", views.globalLives, name="globalLives"),
    path("detailLive/<int:id>/", views.detailLive, name="detailLive"),
    path("logout/", views.logout_user, name="logout"),
    path('api/streamerdashboard/', views.streamerdashboard, name='streamerdashboard-api'),
    path('api/registration/', views.registration_live, name='registration-api'),
    path('incrementClick/<int:id>/', views.increment_click, name='increment-click'),
    path('api/stats/', views.stats, name='stats-api')


]