from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    url(r'^api/token-auth/', obtain_jwt_token),
    url(r'^api/token-refresh/', refresh_jwt_token),
    path('orders', views.OrderView.as_view(), name="orders"),
    path('', views.signin, name="signin"),
]