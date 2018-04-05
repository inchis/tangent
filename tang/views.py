from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from tang.models import Employee
from serializers import EmployeeSerializer
from rest_framework import generics
from rest_framework.test import APIRequestFactory
from rest_framework.permissions import IsAdminUser


class UserList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUser,)

    def get_paginate_by(self):
        """
        Use smaller pagination for HTML representations.
        """
        if self.request.accepted_renderer.format == 'html':
            return 20
        return 100

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        context = dict(request=APIRequestFactory().get('/'))
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, context=context, many=True)
        return Response(serializer.data)


class



