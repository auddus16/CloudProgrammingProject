from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Menu, Category, Order

class MenuList(ListView):
    model = Menu
    ordering = '-pk'

class MenuDetail(DetailView):
    model = Menu


def show_category_menus(request, slug):

    category = Category.objects.get(slug=slug)  # slug 값이 일치하는 카테고리
    menu_list = Menu.objects.filter(category=category)

    context = {
        'category': category,  # 보여줄 카테고리
        'menu_list': menu_list  # 위에서 만든 카테고리와 일치하는 게시글 리스트
    }

    return render(request, 'main_pages/menu_list.html', context)

def add_cart(request, slug, count):
    menu = Menu.objects.get(slug=slug)
    menu.add_count(count)
    menu.update_state()
    menu.save()

    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price * m.count

    context = {
        'total_price' : total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/cart.html', context)

def show_cart_list(request):
    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price * m.count

    context = {
        'total_price' : total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/cart.html', context)


def add_order(request):
    return None