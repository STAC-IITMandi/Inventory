from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Rental, Inventory


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', )


class Comment(forms.ModelForm):

    class Meta:
        model = Rental
        fields = ('comments', )


class Return(forms.ModelForm):

    class Meta:
        model = Rental
        fields = ('returned', )


class RentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset = User.objects.all(), required = False)
    object = forms.ModelChoiceField(queryset = Inventory.objects.all())
    quantity = forms.IntegerField()
    due_date = forms.DateField(widget = forms.SelectDateWidget())

    class Meta:
        model = Rental
        fields = ('user', 'object', 'quantity', 'due_date')
