from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import pla

# Create your views here.
def demo(request):
    # name="india"
    obj=Place.objects.all()
    obj1=pla.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1 })    #,{'obj':name})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"about.html",{'result':res})

def about(request):
    return render(request,"about.html")

#
# def contact(request):
#     return render(request,"contact.html")