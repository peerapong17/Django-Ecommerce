from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from admin_management.forms import SignUpAdminForm


def index(request):
    admins = User.objects.get(is_staff=1)
    print(admins)
    return render(request, "admin/index.html")


def create(request):
    # if request.method == 'POST':
    #     form = SignUpAdminForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         user = User.objects.get(username=username)
    #         # จัด Group
    #         customer_group = Group.objects.get(name="Customer")
    #         customer_group.user_set.add(user)
    #         messages.success(request, "Create account success")
    #         return redirect("signInUser")
    # else:
    #     form = SignUpUserForm()
    return render(request, "admin/create.html")


def update(request):
    pass
    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('home')
    #         else:
    #             return redirect('signUp')
    # else:
    #     form = AuthenticationForm()
    # return render(request, 'auth/signIn.html', {'form': form})


def delete(request):
    pass
    # logout(request)
    # return redirect('signInUser')
