from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from app_user.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request=request,
                context={"mensaje": "Usuario registrado satisfactoriamente."},
                template_name="app_user/login.html",
            )
    #form = UserCreationForm()
    form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="app_user/register.html",
    )



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = "app_home/home.html"
        else:
            template_name = "app_user/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="app_user/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("")