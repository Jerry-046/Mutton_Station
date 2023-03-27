from django.urls import path
from Item import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Index,name='Homepage'),
    path('contact-us/',views.Contact,name='contact-us'),
    path('about-us/',views.aboutus,name='about-us'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
