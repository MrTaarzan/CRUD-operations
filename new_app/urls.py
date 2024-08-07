from django.urls import path

from new_app import views

urlpatterns = [
    path("home",views.home,name="home"),
    path("",views.index,name="index"),
    path("dash",views.dash,name="dash"),
    path("foodname",views.foodname,name="foodname"),
    path("viewfood",views.viewfood,name="viewfood"),
    path("deletefood/<int:id>/",views.deletefood,name="deletefood"),
    path("updatefood/<int:id>/",views.updatefood,name="updatefood")
]
