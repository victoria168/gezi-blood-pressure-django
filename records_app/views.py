from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import auth
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction

from records_app.models import Record
from records_app.serializers import (
    RecordSerializer, MyTokenObtainPairSerializer
)
from records_app.filters import RecordFilter
from records_app.permissions import RecordPermission


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RecordViewSet(viewsets.ModelViewSet):

    queryset = Record.objects.all().order_by('-date')
    serializer_class = RecordSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = RecordFilter
    permission_classes = [RecordPermission, IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Record.objects.filter(user_id=user.id).order_by('-date')

    @action(methods=['post'], detail=False, url_path='create_record',
            url_name='create_record')
    def create_record(self, request):
        user = request.user
        print(user)
        print(request)
        # Check for mandatory fields
        if not (request.data.get('date')):
            error = {'Error': 'date is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('systolic')):
            error = {'Error': 'systolic is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('diastolic')):
            error = {'Error': 'diastolic is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('pulse')):
            error = {'Error': 'pulse is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        Record.objects.create(
            date=request.data.get('date'),
            user_id=user.id,
            systolic=request.data.get('systolic'),
            diastolic=request.data.get('diastolic'),
            pulse=request.data.get('pulse'))

        return Response("created", status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):

    queryset = auth.get_user_model().objects.all()
    permission_classes = []

    @action(methods=['post'], detail=False, url_path='create_user',
            url_name='create_user')
    def create_user(self, request):
        # Check for mandatory fields
        if not (request.data.get('username')):
            error = {'Error': 'username is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('phone_number')):
            error = {'Error': 'Phone Number is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        if not (request.data.get('password')):
            error = {'Error': 'Password is a required field.'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                UserModel = auth.get_user_model()
                # Check if a user with this phone number already exists
                # db field 'email' stores phone number
                if not UserModel.objects.filter(
                        email=request.data.get('phone_number')).exists():

                    # Create user
                    new_user = UserModel(username=request.data["username"],
                                         email=request.data["phone_number"])
                    # Hash the password with set_password()
                    new_user.set_password(request.data["password"])
                    # Save the new user
                    new_user.save()

                response = ('Registration for {} successful,'
                            ' they may now login with their '
                            'username.').format(new_user.get_username())
        except Exception as e:
            error = {'Error': str(e)}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

            # If activation is successful, return 201
        return Response(response, status=status.HTTP_201_CREATED)
