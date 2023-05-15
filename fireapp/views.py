from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
import pyrebase

# Remember the code we copied from Firebase.
# This can be copied by clicking on the settings icon > project settings, then scroll down in your firebase dashboard
config = {
  "apiKey": "AIzaSyDh53l7P_crrB2unpPGwgCBJAaeZrn5XKQ",
  "authDomain": "gogreenstore-inventory.firebaseapp.com",
  "databaseURL": "https://gogreenstore-inventory-default-rtdb.firebaseio.com",
  "projectId": "gogreenstore-inventory",
  "storageBucket": "gogreenstore-inventory.appspot.com",
  "messagingSenderId": "366935662532",
  "appId": "1:366935662532:web:4a327f9d2e762a4aeece91",
  "measurementId": "G-V55YW7PYV3"
}



# here we are doing firebase authentication
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


@login_required(login_url='login')
def fire_index(request):
    # Accessing our Firebase data and storing it in a variable
    distance = database.child('distance').get().val()

    # Get the last value of the "length" key
    last_length = list(distance.values())[-1]
    print("Last length",last_length)


    context = {'distance': distance,'last_length':last_length}

    return render(request, 'fireapp/fire_index.html', context)




