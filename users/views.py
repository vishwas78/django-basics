from django.shortcuts import render
from django.http import HttpResponse

from users.forms import UserAuthForm, UserLoginForm


def register(request):
    print("Entered the register method")
    if request.method == 'POST':
        print("The method is post")
        form = UserAuthForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("Thank you very much")
    else:
        form = UserAuthForm()
        context = {'form': form}
        return render(request, 'users/register.html', context=context)


def login(request):
    form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context=context)
