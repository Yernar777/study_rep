from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
# Create your views here.



def review_functional(request):
    form = ReviewForms()
    form1 = ReviewForms1()
    
    if request.method == 'POST':
        form = ReviewForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form = ReviewForms()

    if request.method == 'POST':
        form1 = ReviewForms1(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('succes')
    return render(request, 'forms.html',{'form': form, 'form1': form1,})


def secces(request):
    return render(request,'succes.html')





def study(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    context = {'form':form,}
    return render(request, 'study.html',context=context)





def login_view(request):
    form = LoginForm(request, data = request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
    context ={'form':form}

    return render(request, 'login.html',context=context)


def logout_view(request):
    logout(request)
    return redirect('login')