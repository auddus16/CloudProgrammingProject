from django.shortcuts import render
import requests

# Create your views here.
from main_pages.models import Menu

def landing(request):
    menu_list= Menu.objects.filter()
    context = {
        'menu_list' : menu_list[::-1]
    }
    return render(request, 'home_pages/home.html', context)

def search(request):
    address1 = request.POST.get('address1')
    address2 = request.POST.get('address2')
    address3 = request.POST.get('address3')

    searching = address1+' '+address2+' '+address3 +' 스타벅스'
    print(searching)
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
    headers = {
        'Host' : 'dapi.kakao.com',
        'Authorization' : "KakaoAK 30d4c7ad19c81602ad8c8f17395208e3"
    }
    places = requests.get(url, headers=headers).json()['documents']
    print(places)
    context = {
        'searching' : searching,
        'store_list' : places
    }
    return render(request, 'home_pages/resultmap.html', context)


def show_map(request):
    return render(request, 'home_pages/map.html')


def show_order(request):
    menu_list = Menu.objects.filter(state=True)

    total_price = 0
    for m in menu_list:
        total_price += m.price * m.count

    context = {
        'total_price': total_price,
        'menu_list': menu_list,
        'store_name' : request.POST.get('store_name'),
        'store_address' : request.POST.get('store_address'),
        'store_number' : request.POST.get('store_number')
    }
    return render(request, 'main_pages/cart2.html', context)