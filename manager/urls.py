
from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.ProfileView)
router.register(r'todos', views.TodosView)
router.register(r'notes', views.NotesView)
router.register(r'jobs', views.JobsView)
router.register(r'employers', views.EmployerView)
router.register(r'seekers', views.SeekerView)
router.register(r'applications', views.ApplicationsView)

urlpatterns = [

    path('', include(router.urls)),
    path('signin', views.SigninView.as_view()),
    path('signout', views.SignoutView.as_view()),

    path('password_change/', views.PasswordChangeView.as_view()),
    path('password_reset/', views.PasswordResetView.as_view()),
    path('password_reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('create_manager', views.CreateManagerView.as_view()),

]
