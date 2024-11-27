from django.shortcuts import render
from .forms import *
from django.shortcuts import render,redirect

# Create your views here.

def study(request):
    return render(request,'study.html')


def review_functional(request):
    if request.method == 'POST':
        form = ReviewForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForms()
        return render(request, 'study.html',{'form': form})