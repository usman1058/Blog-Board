from django.urls import path,include
from .views import views


urlpatterns=[
    path("",include('django.contrib.auth.urls'))
]