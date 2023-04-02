from django.urls import path
from Item import views
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryListView,HomePageView,AddFoodItemView

urlpatterns = [
    path('', HomePageView.as_view(), name='Homepage'),
    path('food-item/', CategoryListView.as_view(), name='Item Page'),
    path('add-food-item/', AddFoodItemView.as_view(), name='add_food_item'),
    path('contact-us/',views.Contact,name='contact-us'),
    path('about-us/',views.aboutus,name='about-us'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
