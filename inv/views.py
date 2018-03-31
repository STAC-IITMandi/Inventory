from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm as LoginForm

from .forms import SignUpForm

def inventory(request):
    if request.user.is_authenticated:
        name = request.user.get_short_name()
        return render(request, 'index.html', {'name': name})
    else:
        return HttpResponseRedirect('/new/')

def new(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form1 = LoginForm(request.POST)
        for i in form1:
            print(i)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('inventory')
        elif form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print("uh")
            if user is not None:
                print("yo")
                login(request, user)
                return redirect('inventory')
    else:
        form = SignUpForm()
        form1 = LoginForm()
    return render(request, 'new.html', {'form': form, 'form1': form1})
