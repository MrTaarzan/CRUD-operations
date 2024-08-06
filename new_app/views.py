from django.shortcuts import render

from new_app.forms import FoodForm


def home(request):
    return render(request,'view.html')
def index(request):
    return render(request,'index.html')
def dash(request):
    return render(request,'dash.html')
# Create your views here.
def foodname(request):
    form = FoodForm
    return render(request,'FoodName.html', {"form":form})