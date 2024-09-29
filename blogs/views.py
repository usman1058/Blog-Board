from django.shortcuts import render
from .models import Blog

# Create your views here.
def home(request):
    posts_list = Blog.objects.all()
    return render(request, 'index.html',{
        'blogs':posts_list,
    }
    )
# def detail(request):
#     post_detail = Blog.objects.all()
#     return render(request, 'detail.html',{
#                   "object":post_detail,
#                   }
#     )            
