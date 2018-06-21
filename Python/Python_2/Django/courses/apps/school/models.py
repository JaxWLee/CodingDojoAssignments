from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def valid(self,post_Data):
        error =[]
        if len(post_Data['name']) < 5:
            error.append("Name of Course must be at least 5 characters long")
        if len(post_Data['description']) < 15:
            error.append("Description must be at least 15 characters long")
        return error

class Description(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    desc = models.OneToOneField(Description)
    
    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course,related_name='comments')


# Create your models here.
