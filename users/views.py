from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = 'home.html'




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

class LoginView(View):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the provided value is an email or a username
        if '@' in username:
            user = authenticate(request, email=username, password=password)
        else:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL
        else:
            return render(request, self.template_name, {'error': 'Invalid credentials'})

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
