from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def valid(self, post_Data):
        error = []
        if len(post_Data['first_name']) == 0:
            error.append('First Name cannot be left blank')
        if len(post_Data['last_name']) == 0:
            error.append('Lirst Name cannot be left blank')
        if len(post_Data['email']) == 0:
            error.append('Email cannot be left blank')
        if not EMAIL_REGEX.match(post_Data['email']):
            error.append('Not a valid email address')
        return error
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()