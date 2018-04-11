from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from tang.models import Employee
from serializers import EmployeeSerializer, UserSerializer
from rest_framework import generics
from rest_framework.test import APIRequestFactory
from rest_framework.permissions import IsAdminUser


class UserList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)

    def get_paginate_by(self):
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 100

    def list(self, request):
        context = dict(request=APIRequestFactory().get('/'))
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, context=context, many=True)
        return Response(serializer.data)


class UserMe(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        context = dict(request=APIRequestFactory().get('/'))
        serializer = UserSerializer(request.user, context=context)
        return Response(serializer.data)