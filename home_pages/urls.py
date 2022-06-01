from django.urls import path

from home_pages import views

urlpatterns = [
    path('', views.landing),

]