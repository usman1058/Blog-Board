from django.urls  import path
from blogs.views import home

urlpatterns = [
    path('', home, name='home'),
    # path("post/<int:pk>/", detail, name="post_detail")
]