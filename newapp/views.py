from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
 return render(request, "index.html")

def travels(request):
    if 'id' not in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["id"])
        # print(user)
        all_trips = Trip.objects.all()
        print(all_trips)
        my_trips = user.trips.all()
        # print(my_trips)
        other_users_trips = all_trips.difference(my_trips)
        context = {
            'user' : user,
            'my_trips' : my_trips,
            'other_users_trips' : other_users_trips,
        }
        return render(request, "travels.html",context)

def showtravels(request,trip_id):
    if 'id' not in request.session:
        return redirect("/")
    else:
        my_trips = Trip.objects.get(id=trip_id)
        users = my_trips.user.all()
        context = {
            "trips" : my_trips,
            "users" : users
        }
    return render(request, "showtravels.html",context)

def addtrip(request):
    if 'id' not in request.session:
        return redirect("/")
    else:
        return render(request, "addtrip.html")


def register(request):
    errors = User.objects.regValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(username=request.POST["username"], name=request.POST["name"], password=hashed_pw.decode())

        request.session['id'] = new_user.id
        return redirect('/travels')


def login(request):
    errors = User.objects.loginValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    else:
        user_list = User.objects.filter(username=request.POST['username'])
        user = user_list[0]
        request.session['id'] = user.id
        return redirect('/travels')



def create_trip(request):
    errors = Trip.objects.tripValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/addtrip')
    else:
        print(request.POST)
        trip=Trip.objects.create(Destination=request.POST["Destination"],Desc=request.POST["Description"],    Travel_start_date=request.POST["Travel_start_date"],Travel_end_date=request.POST["Travel_end_date"],added_by_id=request.session["id"])
        user= User.objects.get(id=request.session['id'])
        user.trips.add(trip)
        return redirect('/travels')


def logout(request):
    request.session.clear()
    return redirect("/")


def jointravels(request, trip_id):
    trip= Trip.objects.get(id=trip_id)
    user= User.objects.get(id=request.session['id'])
    user.trips.add(trip)
    return redirect('/travels')

