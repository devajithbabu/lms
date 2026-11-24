from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from accounts.serializers import UserSerializer
from accounts.models import User
from accounts.models import StudentProfile
from accounts.models import TrainerProfile
from accounts.serializers import StudentProfileSerializer
from accounts.serializers import TrainerProfileSerializer
from accounts.permissions import IsStudent
from accounts.permissions import IsTrainer

# Create your views here.

class TrainerCreateView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_inst = UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data=serializer_inst.validated_data

            instance=User.objects.create_superuser(**cleaned_data)

            serializer_inst=UserSerializer(instance)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

class StudentCreateView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_inst=UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data=serializer_inst.validated_data

            instance=User.objects.create_user(**cleaned_data)

            serializer_inst=UserSerializer(instance)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

class TrainerProfileUpdateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated,IsTrainer]

    def put(self,request):

        form_data=request.data

        trainer_profile_object=TrainerProfile.objects.get(trainer=request.user)

        serializer_inst=TrainerProfileSerializer(data=form_data,instance=trainer_profile_object)

        if serializer_inst.is_valid():

            serializer_inst.save()

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors) 

class StudentProfileUpdateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated,IsStudent]

    def put(self,request):

        form_data=request.data

        student_profile_object=StudentProfile.objects.get(trainer=request.user)

        serializer_inst=StudentProfileSerializer(data=form_data,instance=student_profile_object)

        if serializer_inst.is_valid():

            serializer_inst.save()

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)   

class TrainerDetailView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[]

    def get(self,request):

        instance=TrainerProfile.objects.get(trainer=request.user)

        serializer_inst=TrainerProfileSerializer(instance)

        return Response(data=serializer_inst.data)

class StudentDetailView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[]

    def get(self,request):

        instance=StudentProfile.objects.get(student=request.user)

        serializer_inst=StudentProfileSerializer(instance)

        return Response(data=serializer_inst.data)   