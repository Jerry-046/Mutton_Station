from django.shortcuts import render
from django.views.generic import ListView,TemplateView,CreateView
from .models import CATEGORY,FOODITEM
from django.urls import reverse_lazy
# Create your views here.

def Index(request):
    return render(request,'Item/homepage.html')

def Contact(request):
    return render(request,'Item/contact.html')

def aboutus(request):
    return render(request,'Item/about.html')

class CategoryListView(ListView):
    model = CATEGORY
    template_name = 'Item/itemcat.html'
    context_object_name = 'categories'
    
class HomePageView(TemplateView):
    template_name = "Item/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = CATEGORY.objects.prefetch_related('fooditem_set')
        context['categories'] = categories
        return context


class AddFoodItemView(CreateView):
    model = FOODITEM
    template_name = 'add_food_item.html'
    fields = ['name', 'price', 'image', 'cooking_time', 'category']
    success_url = reverse_lazy('home')

