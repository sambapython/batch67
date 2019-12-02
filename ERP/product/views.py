from django.shortcuts import render
from product.models import Product

# Create your views here.
from django.http import HttpResponse

def fun(request):
	ps = Product.objects.all()

	data = [pro.name for pro in ps]
	data = ";".join(data)
	#return HttpResponse(data)
	return render(request,"product.html",{"products":data})
