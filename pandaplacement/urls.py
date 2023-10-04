from django.contrib import admin
from django.urls import path, include
# from schema_graph.views import Schema
from rest_framework.schemas import get_schema_view
from django.conf import settings
from django.conf.urls.static import static

view = get_schema_view(title="Example API")

urlpatterns = [
    # path("schema/", Schema.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)