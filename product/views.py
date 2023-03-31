from django.shortcuts import render
from .fake_db.products import Fake_Db_Products
from django.http import Http404
# Create your views here.
def product_list_view(request):
    context=dict(
        products=Fake_Db_Products,
    )
    return render(request,'product/products.html',context)
def product_detail_view(request,id):
    result=list(filter(lambda x: (x['id'] == id), Fake_Db_Products))
    
    if result:
        context=dict(
        item=result[0],
        products=Fake_Db_Products,
    )
        return render(request,'product/product_detail.html',context)
    raise Http404

    