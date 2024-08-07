from django.shortcuts import render, redirect

from new_app.forms import FoodForm
from new_app.models import FoodName


def home(request):
    return render(request, 'view.html')


def index(request):
    return render(request, 'index.html')


def dash(request):
    return render(request, 'dash.html')


# Create.
def foodname(request):
    form = FoodForm()
    if request.method == 'POST':
        data = FoodForm(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'FoodName.html', {'form': form})

# Read
def viewfood(request):
    data = FoodName.objects.all()
    return render(request, 'ViewFoodName.html', {'data': data})


# Delete

def deletefood(request, id):
    data = FoodName.objects.get(id=id)
    data.delete()
    return redirect("viewfood")

# Update

def updatefood(request,id):
    data = FoodName.objects.get(id=id)
    form = FoodForm(instance = data)
    if request.method == 'POST':
        data = FoodForm(request.POST,instance=data)
        if data.is_valid():
            data.save()
            return redirect("viewfood")
    return render(request,'UpdateFood.html',{'form':form})
