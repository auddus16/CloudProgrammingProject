from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Menu, Category, Order

# class PostUpdate(LoginRequiredMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content', 'hook', 'head_image', 'attached_file', 'category']
#
#     template_name = "blog/post_form_update.html" # redirect 페이지를 정의하고 싶을 때 오버라이딩.
#     # 오버라이딩 하지 않으면, CreateView(post_form.html)과 같은 곳으로 자동 redirect된다.
#     # post_form.html의 제목 부분을 if문 처리하여 사용하는 방법도 있음.
#
#     def dispatch(self, request, *args, **kwargs): # get에서도 user 권한을 분석하겠다.
#         if request.user.is_authenticated and request.user == self.get_object().author: # 로그인 되어 있니? and 로그인 사용자와 author와 일치하니?
#             return super(PostUpdate, self).dispatch(request, *args, **kwargs)
#         else:
#             raise PermissionDenied
#
# class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): # LoginRequiredMixin : 로그인을 한 상태에서만 글을 쓸 수 있게(인증)
#                                                                         # UserPassesTestMixin : 로그인 한 계정이 글쓰기 권한이 있는가(권한)
#     model = Post
#     fields = ['title', 'content', 'hook', 'head_image', 'attached_file', 'category']
#
#     def test_func(self): # 들어온 사용자의 등급을 확인하는 메소드
#         return self.request.user.is_superuser or self.request.user.is_staff
#
#     def form_valid(self, form):
#         current_user = self.request.user # request에서 user를 받아서 저장
#
#         if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
#             # 로그인 되었을 뿐 아니라, 로그인 된 사용자의 등급을 확인
#             form.instance.author = current_user # form의 instance의 author 자리에 지금 사용자를 넣어서
#
#             return super(PostCreate, self).form_valid(form) # author가 추가된 form상태로 집어넣는다.
#         else:
#             return redirect('/blog/')

class MenuList(ListView):
    model = Menu
    ordering = '-pk'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PostList, self).get_context_data()
    #     context['categories'] = Category.objects.all()
    #     context['count_posts_without_category'] = Post.objects.filter(category=None).count()
    #
    #     return context


class MenuDetail(DetailView):
    model = Menu

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(PostDetail, self).get_context_data()
    #     context['categories'] = Category.objects.all()
    #     context['count_posts_without_category'] = Post.objects.filter(category=None).count()
    #     context['comment_form'] = CommentForm
    #     return context

def show_category_menus(request, slug):

    category = Category.objects.get(slug=slug)  # slug 값이 일치하는 카테고리
    menu_list = Menu.objects.filter(category=category)

    context = {
        'category': category,  # 보여줄 카테고리
        'menu_list': menu_list  # 위에서 만든 카테고리와 일치하는 게시글 리스트
    }

    return render(request, 'main_pages/menu_list.html', context)

def add_cart(request, slug):
    menu = Category.objects.get(slug=slug)
    menu.state = True

    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price

    context = {
        'total_price' : total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/cart.html',context)

def show_cart_list(request):
    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price

    context = {
        'total_price' : total_price,
        'menu_list': menu_list
    }

    return render(request, 'main_pages/cart.html',context)