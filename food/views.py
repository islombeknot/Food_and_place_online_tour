from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect , get_object_or_404
from .models import FoodPlace
from django.views.generic import ListView, DetailView
from .models import FoodPlace, Food ,FoodComment, Category, FavoriteFood
from django.core.paginator import Paginator
from .forms import FoodCommentForm
from django.views import View 

# Create your views here.
def index(request):
    food_places = FoodPlace.objects.all()
    return render(request, 'index.html', {'food_places': food_places})

def food_place_list(request):
    food_places = FoodPlace.objects.all()
    return render(request, 'foodplace_list.html', {'food_places': food_places})

class FoodPlaceDetailView(DetailView):
    food_places = FoodPlace.sorted_by_category()
    model = FoodPlace
    template_name = 'foodplace_detail.html' 
    context_object_name = 'foodplace'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        foodplace = self.get_object()
        context['foods'] = foodplace.food_set.all()  
        context['categorys'] = foodplace.category
        
          
        
        return context



def add_comment(request, food_id):
    food_place = get_object_or_404(FoodPlace, id=id)
    
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        rating = request.POST.get('rating')
        user = request.user  
        
        
        comment = FoodComment.objects.create(user=user, comment=comment_text, rating=rating, foodplace=food_place)
        
        
        return redirect('success_page')  
    else:
        return render(request, 'blog.html')
        

    
def show_comments(request):
    comments = FoodComment.objects.all()
    return render(request, 'comments.html', {'comments': comments})


def blog(request, food_id):
    foodplace = get_object_or_404(FoodPlace, id=food_id)
    comments = FoodComment.objects.filter(foodplace=foodplace)
    paginator = Paginator(comments, 5)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {'comments': comments, 'foodplace': foodplace})