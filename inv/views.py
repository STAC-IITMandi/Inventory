from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm as LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from .forms import SignUpForm
from .models import Inventory, Rental, User

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
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':user.pk,
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            # print(to_email)
            # print(user.pk)
            # print((user.pk))
            # print(message)
            # print(account_activation_token.make_token(user))
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(email=email, password=raw_password)
            # login(request, user)
            # return redirect('inventory')
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

def activate(request, uidb64, token):
    try:
        user = User.objects.get(pk=uidb64)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # print(user)
    account_activation_token.check_token(user, token)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
