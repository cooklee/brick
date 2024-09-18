from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'base.html')
        else:
            return render(request, 'accounts/login.html', {'message':'Invalid username or password'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.create_user(username=username,
                                        first_name=first_name,
                                        last_name=last_name,
                                        password=password,
                                        email=email)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/register.html')

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['old_password']
        error = False
        if not user.check_password(old_password):
            error = True
            messages.add_message(request, messages.ERROR, 'stare hasło jest niepoprawne')
        password = request.POST['password']
        password_confirm = request.POST['confirm_password']
        if password != password_confirm:
            error = True
            messages.add_message(request, messages.ERROR, 'hasła do siebie nie pasują')
        if error:
            return render(request, 'accounts/change_password.html', )
        user.set_password(password)
        user.save()
        return redirect('index')
    return render(request, 'accounts/change_password.html', {'message': 'Passwords do not match'})

@login_required
def delete_user(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        if operation == 'Tak':
            request.user.delete()
            logout(request)
            return redirect('index')
        return redirect('accounts:profile')
    return render(request, 'accounts/delete_user.html')