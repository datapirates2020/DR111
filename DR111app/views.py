from django.shortcuts import render
import pyrebase
from django.contrib import auth


config = {
   'apiKey' : "AIzaSyDpUGQXqG8w0DdxR_EepAa_QhYa24mzb9s",
    'authDomain' : "cpanel-79fb1.firebaseapp.com",
    'databaseURL' : "https://cpanel-79fb1.firebaseio.com",
    'projectId' : "cpanel-79fb1",
    'storageBucket' : "cpanel-79fb1.appspot.com",
    'messagingSenderId' : "187117751635",

}
firebase=pyrebase.initialize_app(config)
authe=firebase.auth()
database=firebase.database()



# Create your views here.
def home(request):
    return render(request,'index.html')
def alumlogin(request):
    return render(request,'alumlogin.html')
def clglogin(request):
    return render(request,'clglogin.html')
def dtlogin(request):
    return render(request,'dtlogin.html')
def postsign(request):
    email=request.POST.get('uname')
    passw = request.POST.get('psw')
    try:
     user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid Credentials"
        return render(request,"alumlogin.html",{"messg":message})
   # print(user['idToken'])
   # session_id=user['idToken']
   # a=authe.get_account_info(user['idToken'])
   # print(a)
   # a=a['users']
   # a=a[0]
    #print(a['localId'])
   # a=a['localId']
   # print(database.child('COLLEGES').child(a).get().val())
   # request.session['uid']=str(session_id)
    return render(request,'welcome.html',{"e":email})
def logout(request):
    auth.logout(request)
    return render(request,'alumlogin.html')
def academic(request):
    return render(request,'academic.html')
def professional(request):
    return render(request,'professional.html')
def alumniregistration_1(request):
    return render(request,'alumniregistration_1.html')