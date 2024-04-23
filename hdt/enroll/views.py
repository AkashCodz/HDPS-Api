from django.shortcuts import render, redirect  
from .forms import userforms       
from .forms import signupform     # Signup    
from django.contrib import messages     # Messages    
from django.contrib.auth.forms import AuthenticationForm  #Login
from django.contrib.auth import authenticate, login, logout

# Signup
def sign_up(request):
    if request.method == 'POST':
        fm=signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully !!')
            fm.save()
    else:
        fm=signupform()
    return render(request, 'enroll/signup.html',{'form':fm})

# Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,'Logged out successfully !!')
                    return redirect('/home/')
        else:
            fm=AuthenticationForm()
        return render(request, "enroll/userlogin.html", {'form':fm})
    else:
        return redirect('/home/')

# Profile

# def user_profile(request):
#     if request.user.is_authenticated:
#         return render(request, 'enroll/profile.html', {'name':request.user})
#     else:
#         return redirect('/login/')
    
# Logout
def user_logout(request):
    logout(request)
    return redirect('login')

# Main file
def home(request):
    if request.user.is_authenticated:
        fn=userforms()
        data={'form':fn}
        return render(request,'enroll/index.html',data)
    else:
        return redirect('/login/')
        # return render(request, 'enroll/profile.html', {'name':request.user})

# custom method for generating predictions

# def getPredictions(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
#     import pickle
#     model = pickle.load(open("enroll/static/enroll/Heart_disease_prediction.sav", "rb"))
#     prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
#     return prediction

import requests
import json   
def result(request):
    age = int(request.POST['age'])
    sex = int(request.POST['sex'])
    cp = int(request.POST['cp'])
    trestbps = int(request.POST['trestbps'])
    chol = int(request.POST['chol'])
    fbs = int(request.POST['fbs'])
    restecg = int(request.POST['restecg'])
    thalach = int(request.POST['thalach'])
    exang = int(request.POST['exang'])
    oldpeak = float(request.POST['oldpeak'])
    slope = int(request.POST['slope'])
    ca = int(request.POST['ca'])
    thal = int(request.POST['thal'])
    URL="http://127.0.0.1:8000/api/"
    data={
            "age":age,
            "sex":sex,
            "cp":cp,
            "trestbps":trestbps,
            "chol":chol,
            "fbs":fbs,
            "restecg":restecg,
            "thalach":thalach,
            "exang":exang,
            "oldpeak":oldpeak,
            "slope":slope,
            "ca":ca,
            "thal":thal
        }
    
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    result = data['Prediction'][0]

    return render(request, 'enroll/result.html', {'result':result})

