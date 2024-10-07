from django.urls  import path
from blogs.views import home,detail,createView,update_post,landing,delete_item


urlpatterns = [
    path('home', home, name='home'),
     path("details/<int:blog_id>/", detail, name="post_detail"),
     path("form",createView,name="createView"),
     path('update/<int:post_id>/', update_post, name='update_post'),
    path('', landing, name='landing'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
]