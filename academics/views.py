from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from academics.models import Course
from academics.serializers import CourseSerializer
from academics.permissions import IsOwner

from accounts.permissions import IsTrainer

# Create your views here.

class CourseListView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):

        instance=Course.objects.filter(trainer_info=request.user)

        serializer_inst=CourseSerializer(instance)

        return Response(data=serializer_inst.data)

class CourseCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsTrainer]

    def Post(self,request):

        form_data=request.data

        serializer_inst=CourseSerializer(data=form_data)

        if serializer_inst.is_valid():

            serializer_inst.save(trainer_info=request.user)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

class CourseRetrieveView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):

        instance=get_object_or_404(Course,id=pk)

        serializer_inst=CourseSerializer(instance)

        return Response(data=serializer_inst.data)

class CourseUpdateDeleteView(APIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]

    def put(self,request,pk=None):

        form_data=request.data

        instance=get_object_or_404(Course,id=pk)

        self.check_object_permissions(request,instance)

        serializer_inst=CourseSerializer(data=form_data,instance=instance)

        if serializer_inst.is_valid():

            serializer_inst.save()

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)

    def delete(self,request,pk=None):

        instance=get_object_or_404(Course,pk=None)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response(data={"message":"deleted"})