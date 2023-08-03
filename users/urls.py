from . import views
from django.urls import path
from .views import HomePageView, SignUpView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]