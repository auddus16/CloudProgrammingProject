from django.urls import path

from home_pages import views

urlpatterns = [
    path('', views.landing),
    path('map/searching/', views.search),
    path('map/', views.show_map)
]