from django.shortcuts import render,redirect
from .models import customers
from django.contrib import messages
from django.db import transaction
# Create your views here.
def home(request):
    
    return render(request,'index.html')

def customer(request):
    details=customers.objects.all().order_by('id')
    return render(request,'customer.html',{'key':details})

def view(request,view_id):
    row=customers.objects.filter(id=view_id)
    row1=customers.objects.exclude(id=view_id)
    if request.method=='POST':
        user=request.POST.get('from')
        to=request.POST.get('to')
        amount=request.POST.get('amount')
        amount=int(amount)
        with transaction .atomic():
            if (amount==0):
                messages.info(request,'Nothing to Transfer')
                return redirect('.')
            else:
                    user1=customers.objects.get(name=user)
                    if (amount>user1.balance):
                        messages.info(request,'No enough balance in your account')
                        return redirect('.')
                    else:
                        user1.balance-=int(amount)
                        user1.save()

                        user2=customers.objects.get(name=to)
                        user2.balance+=int(amount)
                        user2.save()
                        messages.info(request,'Transaction Successful!!!')
                        return redirect('.')
    else: 
     return render(request,'transfer.html',{'views':row,'dd':row1})
                
