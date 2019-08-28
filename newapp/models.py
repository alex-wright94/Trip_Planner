from django.db import models
from datetime import datetime
import re
import bcrypt



class UserManager(models.Manager):
    def regValidator(self, form):
        errors = {}
        if not form['name']:
            errors['name'] = "Please enter your name."
        elif len(form['name']) < 3:
            errors['name'] = "Your name must be at least three characters long."
        
        if not form['username']:
            errors['username'] = "Please enter a username."
        elif len(form['username']) < 3:
            errors['username'] = "Username must be at least three characters long."
        elif User.objects.filter(username=form['username']):
            errors['username']= "Username aleady taken."
        
        if not form['password']:
            errors['password'] = "Please enter a password."
        elif len(form['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        
        if not form['confirm_password']:
            errors['confirm_password'] = "Please confirm your password."
        elif form['confirm_password'] != form['password']:
            errors['confirm_password'] = "Passwords must match."

        return errors

    def loginValidator(self, form):
        errors = {}

        if not form['username']:
            errors['username'] = "Please enter your username."
         
        elif not User.objects.filter(username=form["username"]):
            errors['username'] = "Username not found. Please register."
        else:
            user_list = User.objects.filter(username=form["username"])
            user = user_list[0]
            if not bcrypt.checkpw(form['password'].encode(), user.password.encode()):
                errors['password'] = "Wrong password."
            if not form['password']:
                errors['password'] = "Please enter a password."
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class TripManager(models.Manager):
    def tripValidator(self, form):
        errors = {}
        current_time=datetime.now()
        if not form['Destination']:
            errors['Destination'] = "Please enter a Travel Destination."
        elif len(form['Destination']) < 2:
            errors['Destination'] = "Destination must be at least two characters long."
    
        if not form['Travel_start_date']:
            errors['Travel_start_date'] = "Please enter a start date."
        elif (form["Travel_start_date"]) <str(current_time):
            errors['Travel_start_date'] = "Date cannot be in the past."

        if not form['Travel_end_date']:
            errors['Travel_end_date'] = "Please enter an end date."
        elif form["Travel_end_date"]  <str(current_time):
            errors['Travel_end_date'] = " End Date cannot be in the past."
        return errors
class Trip(models.Model):
    Destination = models.CharField(max_length=255)
    Travel_start_date = models.DateTimeField()
    Desc = models.TextField(max_length=255)
    Travel_end_date= models.DateTimeField()
    user = models.ManyToManyField(User, related_name="trips") 
    added_by = models.ForeignKey(User, related_name="trips_added", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
    def traveler(self):
        return self.user.exclude(id=self.added_by.id)



