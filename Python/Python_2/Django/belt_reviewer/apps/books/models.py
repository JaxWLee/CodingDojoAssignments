from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def validate(self,post_Data):
        error = []
        entry = User.objects.filter(email = post_Data['email'])
        if len(post_Data['name']) == 0:
            error.append('Name cannot be blank')
        if len(post_Data['user_name']) == 0:
            error.append('User Name cannot be blank')
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
    def login(self,post_Data):
        error = []
        user = User.objects.filter(email = post_Data['email'])
        if len(post_Data['email'])  == 0:
            error.append('Email cannot be blank')
        if not EMAIL_REGEX.match(post_Data['email']):
            error.append('Not a valid email')
        if len(post_Data['password']) < 8:
            error.append('Invalid Password')
        if not bcrypt.checkpw(post_Data['password'].encode(), user[0].password.encode()):
                error.append('Incorrect Password')
        return error
class BookManager(models.Manager):
    def validate(self,post_Data):
        error = []
        entry = []
        if len(post_Data['title']) == 0:
            error.append('Title cannot be blank')
        if len(post_Data['add_author']) == 0 and 'author' not in post_Data:
            error.append('Author cannot be blank')
        if len(post_Data['review']) == 0:
            error.append('Review cannot be blank')
        if len(entry) > 0:
            error.append('You already have a review written for this book')
        return error

class User(models.Model):
    user_name = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = BookManager()
    author = models.ForeignKey(Author,related_name="books")

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    book = models.ForeignKey(Book,related_name='reviews')
    user = models.ForeignKey(User,related_name='reviews')

