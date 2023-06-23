from django.shortcuts import render,redirect
from .models import Postdb
from .forms import PostForm,UserLoginForm,UserRegisterForm
from django.views.generic import ListView
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)


# Create your views here.

def base(request):

    return render(request ,'base.html')

@login_required
def home(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list_user')

    context  = {"form":form}

    return render(request,'post_temp/home.html',context)

class post_list(ListView):
    template_name = 'post_temp/post_view.html'
    queryset = Postdb.objects.all()
    context_object_name = 'Postdb'

class post_list_user(ListView):
    template_name = 'post_temp/user.html'
    queryset = Postdb.objects.all()
    context_object_name = 'Postdb'


def login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username ,password = password)
        auth_login(request,user)

        return redirect('home')

    context = {
        'form' : form
    }

    return render(request,'post_temp/login.html',context)



def register(request):

    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit = False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username =user.username,password =password)
        auth_login(request, new_user)
        return redirect('login')

    context = {
        'form' : form
    }

    return render(request,'post_temp/register.html',context)



def logout_view(request):
    logout(request)
    return redirect('/')