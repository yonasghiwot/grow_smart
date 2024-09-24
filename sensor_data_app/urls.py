from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

# URLCONF
urlpatterns = [
    path('home_page', views.home_page, name ='home' ),
    path('', views.dashboard, name='dashboard'),
    #path('', views.home_page, name ='home' ),

    path('sensor_display', views.sensor_display, name = 'sensorData'),
    path('parameters', views.parameters, name = 'parameters'),
    path('parameters_enviroment',views.enviroment_control, name = 'enviroment_control'),
    path('parameters_nft', views.nft_system, name = 'nft_system'),
    path('relays', views.relays, name = 'relays'),
    path('dutch_bucket_1', views.ducth_bucket_1, name="ducth_bucket_1"),
    path('ducth_bucket_2', views.ducth_bucket_2, name="ducth_bucket_2"),
    path('seedling', views.seedling, name="seedling"),
    path('login', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('api', views.api, name ='api' ),
]
