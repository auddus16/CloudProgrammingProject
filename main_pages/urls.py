from . import views
from django.urls import path

urlpatterns = [
    path('cart/<str:slug>/<int:count>/', views.add_cart),
    path('cart/', views.show_cart_list),
    path('order/<str:store>/<int:price>/', views.order),
    path('del/<str:slug>/', views.del_menu),
    path('menu/<str:slug>/', views.MenuDetail.as_view()),
    path('', views.MenuList.as_view()),
    path('order/<int:price>', views.show_ordering),
    path('<str:slug>/', views.show_category_menus),  # <자료형:변수명> -> single_post_page의 매개변수로 넘어간다.
]