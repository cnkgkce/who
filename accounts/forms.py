from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Kullanıcı Adı'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Parola'
    }))



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


