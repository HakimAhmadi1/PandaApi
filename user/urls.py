from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.Seeker_ProfileView)
router.register(r'seeker_information', views.Seeker_InfoView)
router.register(r'ssl_info', views.SSL_InfoView)
# router.register(r'skills', views.SkillsView)
router.register(r'project', views.ProjectsView)
# router.register(r'language', views.LanguagesView)
router.register(r'employment_status', views.Employment_StatusView)
router.register(r'experience', views.ExperienceView)
router.register(r'qualification', views.QualificationView)
router.register(r'jobseeker', views.Job_Seeker_CvView)

urlpatterns = [

    path('', include(router.urls)),
    path('signin', views.SeekerSigninView.as_view()),
    path('signout', views.SeekerSignoutView.as_view()),

    path('password_change/', views.PasswordChangeView.as_view()),
    path('password_reset/', views.PasswordResetView.as_view()),
    path('password_reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('create_seeker', views.CreateSeekerView.as_view()),
    
]
