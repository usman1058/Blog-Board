from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog
from .forms import PostForm
from django.contrib.auth.decorators  import login_required

# Create your views her
@login_required    
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
                  }) 
def landing(request):
    return render(request, 'landing.html'
    )    
@login_required       
def createView(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')

    if request.method == 'POST':
         form = PostForm(request.POST)
         if form.is_valid():
             form_obj = form.save(commit=False)
             form_obj.author = request.user
             form_obj.save()
             return redirect(form_obj.get_absolute_url())
    else:
        form = PostForm()

    return render(request,"create.html",{
        "form":form
    })
@login_required    
def update_post(request, post_id):
    post=Blog.objects.get(pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect(post.get_absolute_url())
    else:
        form=PostForm(instance=post)
        return render(request, 'post_edit.html', {'form':form})
@login_required    
def delete_item(request, item_id):
    item = get_object_or_404(Blog, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')  # Redirect to your item list page or another appropriate page
    return render(request, 'delete.html', {'item': item})

