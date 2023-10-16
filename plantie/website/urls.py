from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('your_plantie', views.your_plantie, name='your_plantie'),
    path('plant_show/', views.plant_show, name='plant_show'),
    path('why_plant/', views.why_plant, name='why_plant'),
    path('logout/', views.logout_user, name='logout'),
    path('signup_user/',views.signup_user, name = 'signup' ),
    
]