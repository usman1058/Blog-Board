from django.urls  import path
from blogs.views import home,detail,createView


urlpatterns = [
    path('', home, name='home'),
     path("details/<int:blog_id>/", detail, name="post_detail"),
     path("form",createView,name="createView")
]