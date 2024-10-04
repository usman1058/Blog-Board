from django.urls  import path
from blogs.views import home,detail,createView,BlogUpdateView,landing


urlpatterns = [
    path('home', home, name='home'),
     path("details/<int:blog_id>/", detail, name="post_detail"),
     path("form",createView,name="createView"),
     path("post/<int:pk>/edit/", BlogUpdateView, name="post_edit"),
    path('', landing, name='landing'),
]