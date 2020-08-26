from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from djangoTest.account.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework import status
from djangoTest.account.models import User
from djangoTest.account.serializers import (
    EquationSerializer, SeriesSerializer, NextNumberSerializer, UserSerializer)


def sum_of_nth(x, n):
    if n == 1:
        return (x**n)
    else:
        return x ** n + sum_of_nth(x, n-1)


class CalculateSum(TokenViewBase):
    permission_classes = (IsAuthenticated,)
    serializer_class = SeriesSerializer

    def post(self, request, *args, **kwargs):

        x = request.data.get('value_of_x')
        n = request.data.get('value_of_n')

        res = sum_of_nth(int(x), int(n))
        response_data = {
            "result": 1/res}
        return Response(response_data, status=status.HTTP_200_OK)


class CalculateEquation(TokenViewBase):
    # permission_classes = (IsAuthenticated,)
    serializer_class = EquationSerializer

    def post(self, request, *args, **kwargs):

        x = int(request.data.get('value_of_x'))
        y = int(request.data.get('value_of_y'))
        a = int(request.data.get('value_of_a'))
        b = int(request.data.get('value_of_b'))
        res1 = ((x + (1/y))**a * (x - (1/y))**b)
        res2 = ((y + (1 / x))**a * (y - (1 / x))**b)
        if res2 == 0:
            res = 0
        else:
            res = res1/res2
        response_data = {
            "result": res}
        return Response(response_data, status=status.HTTP_200_OK)


class CalculateNextNumebrInSeries(TokenViewBase):
    # permission_classes = (IsAuthenticated,)
    serializer_class = NextNumberSerializer

    def post(self, request, *args, **kwargs):

        n = int(request.data.get('value_of_nth'))
        if n % 2 == 0:
            res = n * n - 1
        else:
            res = n * n + 1
        response_data = {
            "result": res}
        return Response(response_data, status=status.HTTP_200_OK)


class RegisterUser(TokenViewBase):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(email=request.data.get('email')).first()

        user_data = {}
        user_data['mobile'] = request.data.get('mobile')
        user_data['email'] = request.data.get('email')
        user_data['password'] = request.data.get('password')

        if user is None:
            serializer = self.get_serializer(data=user_data)
            print('serializer: ', serializer)
            if (serializer.is_valid()):
                user = serializer.save()

                response_data = {
                    "message": "User create successfully"}
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            response_data = {
                "message": "User already exist"}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
