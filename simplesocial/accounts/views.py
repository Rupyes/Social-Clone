from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,DetailView
from django.contrib.auth.models import User

from accounts import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileView(DetailView):
    template_name = "accounts/profile.html"
    model = User
