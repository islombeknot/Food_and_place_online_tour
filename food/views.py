from django.shortcuts import render
from django.shortcuts import render
from .models import FoodPlace
from django.views.generic import ListView, DetailView
from .models import FoodPlace
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')

def food_place_list(request):
    food_places = FoodPlace.objects.all()

   
    return render(request, 'foodplace_list.html', {'food_places': food_places})

class FoodPlaceDetailView(DetailView):
    model = FoodPlace
    template_name = 'foodplace_detail.html' 
    context_object_name = 'foodplace'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foodplace = self.get_object()
        context['foods'] = foodplace.food_set.all()  
        context['categories'] = foodplace.category.foodplace_set.all()  
        return context



# class FoodPlaceListView(ListView):
#     model = FoodPlace
#     template_name = 'foodplace_list.html'
 
#     context_object_name = 'food_places' 
 


