from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import SignUpForm

def inventory(request):
    if request.user.is_authenticated:
        name = request.user.get_short_name()
        return render(request, 'index.html', {'name': name})
    else:
        return HttpResponseRedirect('/login/')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('inventory')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
