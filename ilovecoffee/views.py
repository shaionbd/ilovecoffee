from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Order
from django.contrib.auth.models import User
from .serializers import UserSerializer, OrderSerializer, UserRegistrationSerializer, LoginSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework_jwt import authentication
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings


class OrderListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JSONWebTokenAuthentication]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

    def delete(self, request, id=None):
        order = get_object_or_404(Order, id=id)

        if (order.create_at + timedelta(seconds=15 * 60)) >= timezone.now():
            Order.objects.filter(id=id).update(is_canceled=True)
            return JsonResponse({'message': 'Order has been canceled successfully'}, status=204)
        return JsonResponse({'message': 'Sorry you can not cancel the order'}, status=204)
        # return self.destroy(request, id)


class UserListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def put(self, request, id=None):
        return self.update(request, id)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def delete(self, request, id=None):
        return self.destroy(request, id)

# Login
@csrf_exempt
def loginApi(request):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    serializer = LoginSerializer(data=request.POST)

    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    django_login(request, user)
    return JsonResponse({'token': token}, status=200)


class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JSONWebTokenAuthentication]

    def post(self, request):
        django_logout(request)
        return Response({'message': 'Logout'}, status=200)


@csrf_exempt
def api_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # json_parser = JSONParser()
        data = request.POST
        serializer = UserRegistrationSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    else:
        return JsonResponse({'message': 'No Data Found'}, status=400)


@csrf_exempt
def api_user_detail(request, id):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JSONWebTokenAuthentication,)
    try:
        instance = get_object_or_404(User, id=id)
    except User.DoesNotExist as e:
        return JsonResponse({'message': 'User not found'}, status=404)
    if request.method == 'GET':
        user = get_object_or_404(User, id=id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, status=201)
    elif request.method == 'POST':
        data = request.POST
        serializer = UserSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse({'message': serializer.data}, status=201)
    elif request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)



# login user
def signin(request):
    return render(request, 'auth/signin.html', {})


class OrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JSONWebTokenAuthentication]

    def get(self, request):
        return render(request, 'orders.html', {})
