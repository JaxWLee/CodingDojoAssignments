from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate(self,post_Data):
        error = []
        entry = User.objects.filter(email = post_Data['email'])
        if len(post_Data['first_name']) < 2:
            error.append('First Name must be longer than 2 characters')
        if len(post_Data['last_name']) < 2:
            error.append('Last Name must be longer than 2 characters')
        if not NAME_REGEX.match(post_Data['first_name']):
            error.append('First Name can only contain letters')
        if not NAME_REGEX.match(post_Data['last_name']):
            error.append('Last Name can only contain letters')
        if len(post_Data['email'])  == 0:
            error.append('Email cannot be blank')
        if not EMAIL_REGEX.match(post_Data['email']):
            error.append('Not a valid email')
        if len(post_Data['password']) < 8:
            error.append('Password must be at least 8 characters long')
        if post_Data['password'] != post_Data['confirm']:
            error.append('Passwords must match')
        if len(entry) > 0:
            error.append('This email has already been registered')
        return error


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = UserManager()
