from django.contrib import admin
from django.urls import path,include
from note_book_user import views
from . import views

app_name = "note_book_user"

urlpatterns = [

    path('',views.landingPage,name='landingPage'),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
]
