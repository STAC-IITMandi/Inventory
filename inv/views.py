from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm as LoginForm

from .forms import SignUpForm
from .models import Inventory, Rental

def inventory(request):
    if request.user.is_authenticated:
        user = request.user
        invs = Inventory.objects.all()
        rents = Rental.objects.filter(user = user)
        # if request.method == 'POST':
        #     inventory =
        name = request.user.get_short_name()
        return render(request, 'index.html', {'name': name, 'invs': invs, 'rents':rents})
    else:
        return HttpResponseRedirect('/new/')

def new(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form1 = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('inventory')
        elif 'log' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inventory')
    else:
        form = SignUpForm()
        form1 = LoginForm()
    return render(request, 'new.html', {'form': form, 'form1': form1})
