from django.shortcuts import render
from app_user.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from app_user.forms import UserRegisterForm, UserEditForm, AvatarForm
from django.forms.models import model_to_dict
from app_user.models import Avatar
from django.contrib import messages
from django.shortcuts import redirect
import os


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

def user_update(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.save()

            return redirect('')

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="app_user/user_form.html",
    )     

@login_required
def avatar_load(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid  and len(request.FILES) != 0:
            image = request.FILES['image']
            avatars = Avatar.objects.filter(user=request.user.id)
            if not avatars.exists():
                avatar = Avatar(user=request.user, image=image)
            else:
                avatar = avatars[0]
                if len(avatar.image) > 0:
                    os.remove(avatar.image.path)
                avatar.image = image
            avatar.save()
            messages.success(request, "Imagen cargada exitosamente")
            return redirect('')

    form= AvatarForm()
    return render(
        request=request,
        context={"form": form},
        template_name="app_user/avatar_form.html",
    )        