from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add-list', views.add_list, name="add-list"),
    path('update-list/<int:id>', views.update_list, name="update-list"),
    path('login', views.login, name="login"),
    path('signup', views.signup),
    path('logout', views.signout),
    path('delete-list/<int:id>', views.delete_list),
]