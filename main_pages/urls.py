from . import views
from django.urls import path

urlpatterns = [
    path('', views.MenuList.as_view()),
    path('<str:slug>/', views.show_category_menus),  # <자료형:변수명> -> single_post_page의 매개변수로 넘어간다.
    path('cart/<str:slug>', views.add_cart),
    path('cart/', views.show_cart_list),
    path('menu/<str:slug>/', views.MenuDetail.as_view()),
]