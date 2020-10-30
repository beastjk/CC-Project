from rest_framework import viewsets
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .import models
from .import serializers
from .models import Registration,ProfileEvaluation
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import  auth, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
from bson import json_util
import pickle
import joblib, os
import pandas as pd

ratings = 0

class ProfileViewset(viewsets.ModelViewSet):
    queryset = models.ProfileEvaluation.objects.all()
    serializer_class = serializers.Profile

@api_view(['GET', ''])
def profilee(request, pk):
    queryset = models.ProfileEvaluation.objects.filter(id=pk).values()
    print(type(queryset))
    profileData = list(queryset)
    # profileData = queryset

    mdl = joblib.load('/Users/jayjk/Downloads/cloud-20201007T122819Z-001/load_model.pkl')
    
    print(type(profileData))
    # profileData = json.dumps(profileData, default=json_util.default)

    df = pd.DataFrame(profileData) 
    df = df[['GRE_Score', 'TOEFL_Score', 'SOP', 'LOR', 'CGPA', 'Research']]
    print(df)
    ratings = mdl.predict(df)
    print(ratings)

    dfUni = pd.read_csv('../datasets/University_list.csv',
                        error_bad_lines=False, sep='\t')
    print(dfUni.head())
    print(dfUni['university name'])

    dfUni = pd.DataFrame(
        dfUni.values, columns=['University', 'location', 'fees', 'flag'])
    # dfFlag = dfUni['flag']

    print(type(dfUni))

    dfUni['flag'].replace({1: 5, 2: 4, 4: 2, 5: 1},  inplace=True)

    print(dfUni.head())
    # print(ratings[0])
    dfFilter = dfUni[dfUni['flag'] == ratings[0]]

    # dfFilter = list(dfFilter)

    print((dfFilter))

    # return redirect('listOfUni/')
    return render(request, 'profileView.html', {'profileData': profileData, 'rating': ratings, 'dfFilter': dfFilter})
    # return JsonResponse(profileData)

def profiledelete(request,pk):
    models.ProfileEvaluation.objects.filter(id=pk).delete()
    return(HttpResponse("hello"))



















def index(request):
    if request.method == 'POST':
        first_name = request.POST['field1']
        last_name = request.POST['field2']
        username = request.POST['field3']
        email = request.POST['field4']
        password1 = request.POST['field5']
        password2 = request.POST['field6']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                 print('Username Taken')
                 messages.error(request,'Username already taken')
                 return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('Email Already Exists')
                messages.error(request,'Email already exists')
                return redirect("/")
            else:   
              user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password1) 
              user.save();
              print('User Created')
              register = Registration(first_name=first_name,last_name=last_name,username=username, email=email, password1=password1, password2=password2)
              register.save();
              return redirect('loginn')
        
        else:
             print('Password Not Matching..')
             messages.error(request,'Password did not match')
             return redirect('register')
        #return redirect('login')   
    else:     

         return render(request,"index.html")

def login(request):
    if request.method== 'POST':
                username= request.POST['username']
                password = request.POST[ 'password']

                user = auth.authenticate(username=username, password=password)
                if user is not None:
                        auth.login(request,user)
                        return redirect('register')
                else:
                         messages.error(request,'Invalid Credentials')   
                         print('Invalid Credentials')
                         return redirect('loginn')
    else:
                return render(request, 'loginn.html')


@api_view(['PUT', ])
def profileupdate(request, pk):
    p = ProfileEvaluation.objects.get(id=pk)
    if request.method == "PUT":
        serializer = serializers.Profile(p, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['sucess'] = 'update sucessful'
            return Response(data=data)
        return Response(serializer.errors)
    return(HttpResponse("hello"))
