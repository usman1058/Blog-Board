from django.shortcuts import redirect, render
from .models import Blog
from .forms import CreateBlogForm

# Create your views her
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
    if request.method == 'POST':
         form = CreateBlogForm(request.POST)
         if form.is_valid():
             form_obj = form.save(commit=False)
             form_obj.author = request.user
             form_obj.save()
             return redirect(form_obj.get_absolute_url())
    else:
        form = CreateBlogForm()

    return render(request,"create.html",{
        "form":form
    })
def  BlogUpdateView(request):
    update = CreateBlogForm
    return render(request,"create.html",{
        "update":update
    })




