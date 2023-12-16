from django.urls import path
from . import views
urlpatterns = [
        path("",views.map,name='map'),
        path('routes', views.routes,name='routes'),
        path('map', views.map,name='map'),
        path('import', views.import_ticks,name='import'),
        path('profile', views.profile,name='profile'),
        path('about', views.about,name='about'),
        ]
