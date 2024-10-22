from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menuitem-detail'),
    path('msg/', views.msg, name='msg'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
