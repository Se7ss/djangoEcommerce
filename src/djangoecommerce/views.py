

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm, MyregiterForm, MyloginForm


def home_page(request):
    context = {
        'title': "Hello World!!!!!!!! HOME Page",

    }

    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHH"

    return render(request, 'home_page.html', context)


def about_page(request):

    return render(request, 'about_page.html', {})


def contact_page(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    context = {

        'form': form
    }

    # if request.method=='POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))

    return render(request, 'contact/view.html', context)


def login_page(request):

    form = LoginForm(request.POST or None)

    context = {
        'form': form

    }

    print("User Logged in isss:")
    # clsprint(request.user.is_authenticated)

    if form.is_valid():
        print(form.cleaned_data)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username,
                            password=password)

        print(user)
        # print(request.user.is_authenticated)

        if user is not None:
            # print(request.user.is_authenticated)
            login(request, user)
            # Redirect to success page
            return redirect(login_page)
        else:
            # Return Error 'invalid Login Page'
            print("Error USER is not LOGGED in")

    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

        return redirect(register_page)

    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)


def myregister_page(request):

    form = MyregiterForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = User.objects.create_user(username, email, password)
        print(new_user)

        return redirect(myregister_page)

    context = {

        'form': form

    }

    return render(request, "myauth/myregister_page.html", context)


def mylogin_page(request):

    form = MyloginForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(request, username=username,
                            password=password)

        print(user)

        if user is not None:

            login(request, user)

            return redirect(home_page)
        else:
            print("user in not Loggined ")

    context = {

        'form': form

    }

    return render(request, "myauth/mylogin_page.html", context)
