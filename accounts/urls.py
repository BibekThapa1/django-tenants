from django.contrib import admin
from django.urls import path
from .views import RegisterConsultancyView,DemoView

urlpatterns = [
    path('registerConsultancy/',RegisterConsultancyView.as_view(),name="register"),
    path('demo/',DemoView.as_view(),name="demo")
]
