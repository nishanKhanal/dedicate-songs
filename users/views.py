from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import CustomUser
from .forms import CustomUserCreationForm
# Create your views here.

class SignUpView(CreateView):
    success_url = reverse_lazy('login')
    form_class = CustomUserCreationForm
    template_name = "users/signup.html"


    def form_valid(self, form):
        self.object = form.save()
        full_name = self.request.POST['full_name']
        last_name = full_name.split(' ')[-1]
        first_name = full_name.replace(last_name,'')[:-1]
        self.object.first_name = first_name
        self.object.last_name = last_name
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())