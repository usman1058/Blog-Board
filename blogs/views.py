from django.shortcuts import render
from .models import Blog
from .forms import CreateBlogForm

# Create your views here.
def home(request):
    posts_list = Blog.objects.all()
    return render(request, 'index.html',{
        'blogs':posts_list,
    }
    )
def detail(request,blog_id):
    post_detail = Blog.objects.get(id=blog_id)
    print(post_detail.title)

    return render(request, 'detail.html',{
                  "object":post_detail,
                  }
    )            
def createView(request):
    form = CreateBlogForm()
    return render(request,"create.html",{
        "form":form
    })
