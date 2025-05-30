from django.contrib import admin
from django.urls import path, include
from authentication import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('uploadfile/', include("uploadfile.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
