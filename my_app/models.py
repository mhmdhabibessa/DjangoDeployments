from typing import Any
from django import forms

from django.db import models
import re	# the regex module

class MovieManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 5:
            errors["title"] = "Movie name should be at least 5 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Movie description should be at least 10 characters"
        # if len(postData['image_file']) < 3:
        #     errors["image_file"] = "Image is requeird"
        if not EMAIL_REGEX.match(
            postData['email']):
            errors['email'] = 'Inavlid email'
        return errors

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        db_emails = User.objects.filter(email = post_data['email'])
        if len(db_emails) > 0:
            errors['email'] = "This Email is already in use!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email address!"
            
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters"
        if len(post_data['password']) < 8 :
            errors['password'] = "Password must be at least 8 characters"
        # if post_data['password'] != post_data['confirm_password'] :
            # errors['confirm_password'] = "Your password didn't match!"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # movies = []
    
class Actor(models.Model):
    name = models.TextField()
    age = models.CharField(max_length=45)     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField(null=True)
    duration = models.IntegerField() 
    image= models.TextField(null=True)
    email = models.CharField(max_length=45,null=True)
    category = models.ForeignKey(Category, related_name="movies", on_delete = models.CASCADE)
    actors = models.ManyToManyField(Actor,related_name="movies_actors")
    image_file = models.ImageField(upload_to='movie_images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MovieManager()
    
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration',  'email', 'category','image_file']
    




    