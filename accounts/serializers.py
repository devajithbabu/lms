from rest_framework import serializers

from accounts.models import User
from accounts.models import TrainerProfile
from accounts.models import StudentProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","username","password","phone","email","role"]

class TrainerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=TrainerProfile

        fields="__all__"

        read_only_fields=["id","trainer","date_joined"]

class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=StudentProfile

        fields="__all__"

        read_only_fields=["id","student","date_joined"]
