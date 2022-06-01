from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Menu, Category, Order, Customer, Coupon


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


def show_ordering(request, price): # 결제 화면으로 넘어가는 메소드
    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price * m.count
    have_coupon = False
    context = {
        'have_coupon' : have_coupon,
        'total_price': total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/order.html', context)


def del_menu(request, slug):
    menu = Menu.objects.get(slug=slug)
    menu.set_count_0()
    menu.update_state_false()
    menu.save()

    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price * m.count
    have_coupon = False
    context = {
        'have_coupon': have_coupon,
        'total_price': total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/cart.html', context)

def order(request, store, price):
    order = Order(store=store, price=price)
    order.save()

    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price * m.count

    for m in menu_list: # 초기상태로 되돌리기
        m.update_state_false()
        m.set_count_0()
        m.save()

    context = {
        'order' : order,
        'total_price': total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/order.html', context)

# def show_coupon_list(request, phone): # 쿠폰리스트 검색
#
#     phone = '+821'+phone[3:]
#
#     coupon_list = None
#     have_coupon =False
#
#     if Coupon.objects.filter(phone=phone):
#         phone = '+821' + phone[3:]
#         coupon_list = Coupon.objects.filter(phone=phone)
#         have_coupon = True
#
#     context = {
#         'have_coupon': have_coupon,
#         'coupon_list': coupon_list
#     }
#
#     return render(request, 'main_pages/order.html', context)
#
# def add_stamp_list(request, phone): # 스탬프 적립
#     menu_list = Menu.objects.filter(state=True)
#
#     total_cnt = 0
#     total_price =0
#     for m in menu_list:
#         total_cnt +=  m.count
#         total_price += m.price * m.count
#
#     get_coupon = False
#     get_stamp = False
#     customer = None
#     if Customer.objects.filter(phone=phone).exists():
#         customer = Customer.objects.filter(phone=phone)
#         customer.add_stamp(total_cnt)
#         customer.save()
#         get_stamp = True
#
#         #customer = Customer.objects.filter(phone=phone)
#         if customer.get_stamp()>=10:
#             customer.minus_stamp()
#             new_coupon = Coupon(customer=customer)
#             new_coupon.save()
#             get_coupon = True
#
#     context = {
#         'total_price': total_price,
#         'menu_list': menu_list,
#         'get_coupon' : get_coupon,
#         'get_stamp' : get_stamp,
#         'customer' : customer
#     }
#     return render(request, 'main_pages/order.html', context)

