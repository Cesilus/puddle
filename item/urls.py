from django.urls import path

from . import views
from .views import  purchase_item, shipping_info_view,confirm_purchase

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    
    path('item/<int:pk>/purchase/', purchase_item, name='purchase_item'),
    path('item/<int:pk>/shipping/', shipping_info_view, name='shipping_info'),
    path('<int:pk>/confirm-purchase/', confirm_purchase, name='confirm_purchase'),

]
