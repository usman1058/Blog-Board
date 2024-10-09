from django.urls import path,include
from . import views

# from .views import views


urlpatterns=[
    path("",include('django.contrib.auth.urls')),
      path('signup/', views.signUpView, name='sign-up'),
]