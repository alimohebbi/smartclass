from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Student(User):
    pass


class Staff(User):
    phone_number = models.CharField(max_length=12)
    pass