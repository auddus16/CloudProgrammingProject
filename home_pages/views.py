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
        'searching' : searching
    }
    return render(request, 'home_pages/home.html')


def show_map(request):
    return render(request, 'home_pages/map.html')