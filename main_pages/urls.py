from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuList.as_view()),
    path('<int:pk>/', views.MenuDetail.as_view()),  # <자료형:변수명> -> single_post_page의 매개변수로 넘어간다.
]