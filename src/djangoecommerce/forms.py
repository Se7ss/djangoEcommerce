from django.contrib.auth import get_user_model
from django import forms
from django.forms.widgets import EmailInput


class ContactForm(forms.Form):

    fullname = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "yourFullNAme"}))
    email = forms.EmailField(widget=EmailInput(
        attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'bla'}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail")

        return email


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'form-control'

    }))


User = get_user_model()


class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={

        'class': 'form-control'

    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={

        'class': 'form-control'

    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={

        'class': 'form-control'

    }))

    def clean_username(self):

        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError(f"User {username} Already Exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already Exists")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 != password:
            raise forms.ValidationError("Passwords Must Match")

        return data


class MyloginForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class MyregiterForm(forms.Form):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):

        data = self.cleaned_data

        password = data["password"]
        password2 = data["password2"]

        if password != password2:
            raise forms.ValidationError("Passwords Must Match")

        return data
        # print(data)

    def clean_username(self):
        data = self.cleaned_data
        username = data["username"]
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("User exists")
        return username
