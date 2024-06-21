from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemViewSet, RegisterView, LoginView

# Initialize the router
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    # Include the router-generated URLs
    path('', include(router.urls)),
    
    # Add paths for registration and login
    path('register/', RegisterView.as_view(), name='register'),
    path('login/',  LoginView.as_view(), name='login'),
]
