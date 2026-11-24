from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail

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

    date_of_birth=models.DateField(null=True)

    bio_data=models.TextField(null=True)

    profile_pic=models.ImageField(upload_to="cover_pics",null=True)

    department=models.CharField(max_length=200,null=True)

    linkedin=models.URLField(null=True)



class StudentProfile(models.Model):

    student=models.OneToOneField(User,on_delete=models.CASCADE)

    qualification=models.CharField(max_length=150,null=True)

    date_joined=models.DateField(auto_now=True)

    date_of_birth=models.DateField(null=True)

    bio_data=models.TextField(null=True)

    passout_year=models.CharField(max_length=200,null=True)

    skills=models.CharField(max_length=200,null=True)

    address=models.CharField(max_length=200,null=True)

    profile_pic=models.ImageField(upload_to="cover_pics",null=True)

    linkedin=models.URLField(null=True)

    github=models.URLField(null=True)

def create_trainer_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "trainer":

        TrainerProfile.objects.create(trainer=instance)

post_save.connect(create_trainer_profile,sender=User)

def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)