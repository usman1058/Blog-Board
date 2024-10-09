from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def signUpView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {
        "form": form
    })
# Create your views here.
