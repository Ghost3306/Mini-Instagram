from django.urls import path
from homepage import views

urlpatterns = [
   path('',views.landing_page),
]
