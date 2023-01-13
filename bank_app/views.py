from django.shortcuts import render,redirect
from .models import customers
# Create your views here.
def home(request):
    
    return render(request,'index.html')

def customer(request):
    details=customers.objects.all().order_by('id')
    return render(request,'customer.html',{'key':details})