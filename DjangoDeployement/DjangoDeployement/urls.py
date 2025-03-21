from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home, name="home"),
    path('result/', views.result, name="result"),
    path('prediction/', views.prediction, name="prediction"),
    path('about/', views.about, name="about")
]
