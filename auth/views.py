from .forms import SignUpUserForm
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def sign_up_user(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            # จัด Group
            customer_group = Group.objects.get(name="Customer")
            customer_group.user_set.add(user)
            messages.success(request, "Create account success")
            return redirect("signInUser")
    else:
        form = SignUpUserForm()
    return render(request, "auth/sign_up.html", {'form': form})


def sign_in_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('signUp')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/sign_in.html', {'form': form})


def sign_out_user(request):
    logout(request)
    return redirect('signInUser')
