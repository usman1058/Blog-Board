from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=get_user_model()
        fields=('username','email','age','bio')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # username field
        self.fields['username'].widget.attrs.update({
            'class': 'form-control'
        })
        
        # password1 field
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control'
        })
        
        # password2 field
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control'
        })