"""grow_smart_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from data_visualization_app import views
  

urlpatterns = [    
    
    path('', views.data_visualization_app, name='data'),
    path('api/data', views.get_data, name='api_data'),
    path('charts/data', views.ChartData.as_view(), name="charts"),
    path('onemonths/', views.OneMonths.as_view()),
    path('twomonths/', views.TwoMonths.as_view()),
    path('threemonths/', views.ThreeMonths.as_view()),
    path('humidity_data', views.humidity, name='humidity_data'),
    path('humidityonemonths/', views.HumidityOneMonths.as_view()),
    path('humiditytwomonths/', views.HumidityTwoMonths.as_view()),
    path('humiditythreemonths/', views.HumidityThreeMonths.as_view()),
    path('ph_data', views.ph, name='ph_data'),
    path('phonemonths/', views.phOneMonths.as_view()),
    path('phtwomonths/', views.PhTwoMonths.as_view()),
    path('phthreemonths/', views.PhThreeMonths.as_view()),
    path('ec_data', views.ec, name='ec_data'),
    path('econemonths/', views.EcOneMonths.as_view()),
    path('ectwomonths/', views.EcTwoMonths.as_view()),
    path('ecthreemonths/', views.EcThreeMonths.as_view()),
    
]

urlpatterns += staticfiles_urlpatterns()
