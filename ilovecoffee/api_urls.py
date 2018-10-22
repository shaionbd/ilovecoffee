from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/login', views.loginApi),
    path('auth/logout', views.LogoutApiView.as_view()),
    path('orders', views.OrderListView.as_view()),
    path('order/<int:id>', views.OrderListView.as_view()),
    path('users', views.api_users),
    path('user/<int:id>', views.api_user_detail),
    # path('users', views.UserListView.as_view()),
    path('auth/user/<int:id>', views.UserListView.as_view()),
]