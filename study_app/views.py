from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect

# Create your views here.

def study(request):
    
    return render(request,'study.html')


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