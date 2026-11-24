from django.db import models

from accounts.models import User

# Create your models here.

class Course(models.Model):

    title=models.CharField(max_length=200)

    short_description=models.TextField()

    detailed_description=models.TextField()

    thumbnail=models.ImageField()

    duration=models.CharField(max_length=100)

    COURSE_LEVEL_OPTIONS=(
        ("beginner","Beginner"),
        ("intermediate","Intermediate"),
        ("advanced","Advanced")
    )

    course_level=models.CharField(max_length=150, choices=COURSE_LEVEL_OPTIONS, default="beginner")

    STATUS_LEVEL_OPTIONS=(
        ("draft","Draft"),
        ("published","Published"),
        ("archived","Archived")
    )

    status=models.CharField(max_length=150, choices=STATUS_LEVEL_OPTIONS,default="draft")

    last_updated_date=models.DateField(auto_now=True)

    trainer_info=models.ForeignKey(User,on_delete=models.CASCADE)