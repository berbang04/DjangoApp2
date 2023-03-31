from django.shortcuts import render
from django.http import HttpResponse,Http404
from random import randint
from .fake_db.page import Fake_db_pages

# Fake_Db_projects=[
#      f"https://picsum.photos/id/{id}/100/80" for id in range(21,29)
#      ]
Fake_home_projects=[
    f"https://picsum.photos/id/{id}/1200/400" for id in range(321,325)
]
Fake_home_cards=[
    f"https://picsum.photos/id/{id}/500/500?blur=2" for id in range(120,129)

]
def home(request):
    page_view=""
    context=dict(
        page_view=page_view,
        # Fake_Db_projects=Fake_Db_projects,
        Fake_home_projects=Fake_home_projects,
        Fake_home_cards=Fake_home_cards,
    )
    return render(request,"page/home_page.html",context)
def about(request):
    page_view="about"
    hero_title="About Us"
    hero_content=" Django, Python Programlama Dili için hazırlanmış ve BSD lisansı ile lisanslanmış yüksek seviyeli bir web çatısıdır. Basit kurulumu ve kullanımı, detaylı hata raporu sayfaları ve sunduğu yeni arayüz kodlama yöntemleriyle diğer sunucu yazılımı ve çatılardan kendini ayırmaktadır. "
    
    context=dict(
        page_view=page_view,
        hero_title=hero_title,
        hero_content=hero_content,
        # Fake_Db_projects=Fake_Db_projects,
    )

    return render(request,"page/about.html",context)
def contact(request):
    page_view="contact"
    hero_title="Contact Us"
    hero_content="İngilizceden çevrilmiştir-Flask, Python ile yazılmış bir mikro web çerçevesidir. Belirli araçlar veya kitaplıklar gerektirmediğinden mikro çerçeve olarak sınıflandırılır. Veritabanı soyutlama katmanı, form doğrulama veya önceden var olan üçüncü taraf kitaplıklarının ortak işlevler sağladığı diğer bileşenlere sahip değildir."
    context=dict(
        page_view=page_view,
        hero_title=hero_title,
        hero_content=hero_content,
        # Fake_Db_projects=Fake_Db_projects,
    )

    return render(request,"page/contact.html",context)
def vision(request):
    page_view="vision"
    context=dict(
        page_view=page_view,
        # Fake_Db_projects=Fake_Db_projects,
    )

    return render(request,"page/vision.html",context)
def page_view(request,slug):
    result=list(filter(lambda x: (x['url'] == slug), Fake_db_pages))
    context=dict(
        page_view=result[0]['title'],
        # Fake_Db_projects=Fake_Db_projects,
        detail=result[0]['detail'],
    )
    if result:
        return render(request,"page/page_detail.html",context)
    raise Http404


# Create your views here.
