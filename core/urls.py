from django.contrib.auth import views as auth_views
from django.urls import path
from .views import change_password
from django.views.generic import TemplateView



from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='core/change_password.html')),
    path('update_user/', views.update_user, name='update_user'),


    
]
