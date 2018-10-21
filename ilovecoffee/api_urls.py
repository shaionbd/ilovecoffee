from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/login', views.loginApi),
    path('auth/logout', views.LogoutApiView.as_view()),
    path('generic/orders', views.OrderListView.as_view()),
    path('generic/orders/<int:id>', views.OrderListView.as_view()),
    path('users', views.api_users),
    path('user/<int:id>', views.api_user_detail),
    path('generic/users', views.UserListView.as_view()),
    path('generic/users/<int:id>', views.UserListView.as_view()),
]