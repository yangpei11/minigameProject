from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("GetVerifyCode", views.getVerifyCode, name = "getVerifyCode"),#获得验证码
    path("Login", views.login, name = "login"),
    path("SaveData", views.saveData, name ="SaveData")
]
