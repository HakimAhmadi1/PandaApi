
from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'', views.index)
router.register(r'', views.ProfileView)
router.register(r'company_info', views.CompanyInfoView)
router.register(r'todo_list', views.Todo_ListView)
router.register(r'notes', views.Notes_ListView)
router.register(r'jobs', views.JobsView)
router.register(r'jobs_preferences', views.Job_PreferencesView)
router.register(r'job_prescreen', views.Job_PreScreenView)
router.register(r'application', views.Application)
router.register(r'job_review', views.Job_ReviewsView)
router.register(r'notifications', views.NotificationListView)


urlpatterns = [
    path('', include(router.urls)),

    path('download_cv/<int:cv_id>',views.Download_CV.as_view(), name="download_cv"),
    path('create_employer', views.CreateEmployerView.as_view(), name="create_employer"),
    path('signin', views.SigninView.as_view(), name="employer_signin"),
    path('signout', views.SignoutView.as_view(), name="employer_signout"),

    path('password_change/', views.PasswordChangeView.as_view()),
    path('password_reset/', views.PasswordResetView.as_view()),
    path('password_reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
]

