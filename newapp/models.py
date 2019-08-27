from django.db import models
import re
from datetime import datetime
import bcrypt

NOW  = str(datetime.now())
EMAIL_REGEX= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# Create your models here.
class UserManager(models.Manager):
    def regValidator(self, form):
        
        errors={}
        First_Name= form['First_Name']
        Last_Name=form['Last_Name']
        Email=form['Email']
        Password=form['Password']
        Password_Confirm=form['Password_Confirm']



        if not First_Name:
            errors["First_Name"]="Please enter a first name."
        elif len (First_Name)<2:
            errors['First_Name'] = "First name must be at least two characters."
        elif not First_Name.isalpha():
            errors['First_Name']="First name must contain letters only."




        if not Last_Name:
            errors['Last_Name'] = "Please enter a last name."
        elif len(Last_Name) < 2:
            errors['Last_Name'] = "Last name must be at least two characters."
        elif not Last_Name.isalpha():
            errors['Last_Name'] = "Last name must contain letters only."


    
        if not Email:
            errors['Email']= "Please enter an email."
            elif not EMAIL_REGEX.match(Email):
            errors['Email'] = "Please enter a valid email."
        elif User.objects.filter(Email=Email):
            errors['Email'] = "Email already in database. Please login."


        if not Birthday:
            errors['Birthday'] = "Please enter a birthday."
        elif Birthday > NOW:
            errors['Birthday'] = "You cannot be born in the future."

        
        if not Password:
            errors['Password'] = "Please enter a password."
        elif len(Password) < 8:
            errors['Password'] = "Password must be at least 8 characters."


        if not Password_Confirm:
            errors['Password_Confirm'] = "Please enter a confirm password."
        elif password != Password_Confirm:
            errors['Password_Confirm'] = "Passwords must match."


            return errors

    def loginValidator(self,form):
        errors{}

        Email=form['Email']
        Password=form['Password']

        if not Email:
            errors['Email'] = "Please enter an email."
        elif not EMAIL_REGEX.match(Email):
            errors['Email'] = "Please enter a valid email."
        elif not User.objects.filter(Email=Email):
            errors['Email'] = "Email not found. Please register."
        else:
            User_list = User.objects.filter(Email=Email)
            User = User_list[0]
            if not bcrypt.checkpw(password.encode(), user.password.encode()):
                errors['password'] = "Wrong password."










        return errors





class User(models.Model):
    First_Name= models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Birthday=models.DateTimeField()
    Password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Password_Confirm= models.CharField(max_length=100)
    objects = UserManager