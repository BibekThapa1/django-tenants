from django.contrib import admin
from django.urls import path, include
from accounts.views import RegisterConsultancyView,DemoView

urlpatterns = [
    path('admin/',admin.site.urls),
    path('registerConsultancy/',RegisterConsultancyView.as_view(),name="registerUser"),
    path('demo/',DemoView.as_view(),name="demoview")
]
