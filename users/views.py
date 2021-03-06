from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from users.forms import UserAuthForm, UserLoginForm


def register(request):
    print("Entered the register method")
    if request.method == 'POST':
        print("The method is post")
        form = UserAuthForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return HttpResponse("Thank you very much")
        else:
            context = {'form': form}
            return render(request, 'users/register.html', context=context)
    else:
        form = UserAuthForm()
        context = {'form': form}
        return render(request, 'users/register.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print("username: ", data['username'], ', password: ', data['password'])
            user = authenticate(request=request, username=data['username'], password=data['password'])
            print('user: ', user)
            if user is not None:
                login(request, user=user)
                return HttpResponse('This is the profile page')
            else:
                return HttpResponse('The user is not registered')
        else:
            context = {'form': form}
            return render(request, 'users/login.html', context=context)

    else:
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context=context)


def me(request):
    print(request.user)

    return HttpResponse(request.user.username)


def logout_view(request):
    logout(request)
    return HttpResponse("You have been logged out :)")
