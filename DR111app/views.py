from django.shortcuts import render
import pyrebase
from django.contrib import auth








config = {
    'apiKey' : "AIzaSyAFpFI-PLwWMQBQl1Sa8Xcr8lDtX8HjACw",
    'authDomain': "alumni-tracking-dr111.firebaseapp.com",
    'databaseURL': "https://alumni-tracking-dr111.firebaseio.com",
    'projectId': "alumni-tracking-dr111",
    'storageBucket': "alumni-tracking-dr111.appspot.com",
    'messagingSenderId': "114811974328",
    'appId': "1:114811974328:web:c9b17d3197d46edf2d3a4d",
    'measurementId': "G-H6GZ2F9TNS"

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
def Cancel(request):
    return render(request,'index.html')
def password_reset(request):
    return render(request,'password_reset_form.html')
def password_reset_done(request):
    return render(request,'password_reset_done.html')
def password_reset_confirm(request):
    return render(request,'password_reset_confirm.html')
def password_reset_complete(request):
    return render(request,'password_reset_complete.html')
def register(request):
    return render(request,'alumniregistration_1.html')
def academic(request):
    return render(request,'academic.html')
def professional(request):
    return render(request,'professional.html')
def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('password')

    user=authe.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"name":name,"status":"1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request,"alumlogin.html")


