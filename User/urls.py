from django.urls import path
from User import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
