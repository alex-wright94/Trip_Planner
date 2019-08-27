from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
 return render(request, "index.html")


def register(request):
    print(request.POST)
    errors = User.objects.regValidator(request.POST)
    print(errors)


    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed_pw= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        newuser = User.objects.create(First_name=request.POST['First_Name'], Last_Name=request.POST['Last_Name'], Email=request.POST['Email'],Password=hashed_pw.decode(), bday=request.POST['bday'])

        request.session['id']= newuser.id
        return redirect("/success")

def login(request):
    errors=User.objects.loginValidator(request.POST)

    if errors:
        for key, value in error.items():
            messages.error(request, value)
            return redirect('/success')
    else:
        User_list= User.objects.filter(Email=request.POST['Email'])
        User=User_list[0]
        request.session['id']= user.id
        return redirect('/success')




def logout(request):
    request.session.clear()
    return redirect("/")


def success(request):
    if 'id' not in request.session:
        return redirect ("/")
    else:
        context = {
            'user' : User.objects.get(id=request.session['id'])
        }
    return render(request, "success.html", context)