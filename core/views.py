from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from item.models import Category,Item 
from .forms import SingUpForm,LoginForm

def index(request):
    items = Item.objects.filter(is_sold=False) [0:6]
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'items':items,
        'categories':categories,
    })

def contact(request):
    return render(request,'core/contact.html')

def singup(request):

    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/login/")
            
    else:    
        form = SingUpForm()
    return render(request,'core/singup.html',{
        'form':form,
    })

def user_logout(request):

    logout(request)

    return redirect('/')