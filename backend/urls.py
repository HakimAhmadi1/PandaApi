from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('user/', include('user.urls')),
    path('employer/', include('employer.urls')),
    path('manager/', include('manager.urls')),
    path('contactus/', views.ContactUsView.as_view(), name= "contactus")

]