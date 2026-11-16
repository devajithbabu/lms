from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=12)

    ROLE_CHOICES=(
        ("student","student"),
        ("trainer","trainer")
    )

    role=models.CharField(max_length=100)

class TrainerProfile(models.Model):

    trainer=models.OneToOneField(User,on_delete=models.CASCADE)

    qualification=models.CharField(max_length=150,null=True)

    date_joined=models.DateField(auto_now=True)

class StudentProfile(models.Model):

    student=models.OneToOneField(User,on_delete=models.CASCADE)

    qualification=models.CharField(max_length=150)

    enrolled_courses=models.CharField(max_length=200)

    date_joined=models.DateField(auto_now=True)