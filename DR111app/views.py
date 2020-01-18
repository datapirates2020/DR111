from django.shortcuts import render, redirect
import pyrebase
from django.contrib import auth

config = {
    'apiKey': "AIzaSyAFpFI-PLwWMQBQl1Sa8Xcr8lDtX8HjACw",
    'authDomain': "alumni-tracking-dr111.firebaseapp.com",
    'databaseURL': "https://alumni-tracking-dr111.firebaseio.com",
    'projectId': "alumni-tracking-dr111",
    'storageBucket': "alumni-tracking-dr111.appspot.com",
    'messagingSenderId': "114811974328",
    'appId': "1:114811974328:web:c9b17d3197d46edf2d3a4d",
    'measurementId': "G-H6GZ2F9TNS"

}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


# Create your views here.
def home(request):
    return render(request, 'index.html')


def alumlogin(request):
    return render(request, 'alumlogin.html')


def clglogin(request):
    return render(request, 'clglogin.html')


def dtlogin(request):
    return render(request, 'dtlogin.html')


def postsign(request):
    email = request.POST.get('uname')
    passw = request.POST.get('psw')
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials"
        return render(request, "alumlogin.html", {"messg": message})
    uid = user['localId']
    accountInfo = authe.get_account_info(user['idToken'])
    accountInfo = accountInfo['users']
    accountInfo = accountInfo[0]
    accountInfo = accountInfo['emailVerified']
    if accountInfo:
        return render(request, 'welcome.html', {"e": email})
    return render(request, "alumlogin.html", {"messg": 'Email ID is not verified '})


# print(user['idToken'])
# a=authe.get_account_info(user['idToken'])
# print(a)
# a=a['users']
# a=a[0]
# print(a['localId'])
# a=a['localId']
# print(database.child('COLLEGES').child(a).get().val())


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return redirect('/')


def Cancel(request):
    return render(request, 'index.html')


def password_reset(request):
    return render(request, 'password_reset_form.html')


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')


def register(request):
    return render(request, 'alumniregistration_1.html')


def academic(request):
    return render(request, 'academic.html')


def professional(request):
    return render(request, 'professional.html')


def collsearch(request):
    return render(request, 'collsearch.html')


def dir(request):
    return render(request, 'dir.html')


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')
    college = request.POST.get('clgname')
    passing_year = request.POST.get('passout')
    branch = request.POST.get('branch')
    print(college)
    user = authe.create_user_with_email_and_password(email, passw)
    uid = user['localId']
    authe.send_email_verification(user['idToken'])
    data = {"NAME": name, "EMAIL": email, "REGISTERED": False, "PASSOUT": passing_year, 'BRANCH': branch, }
    database.child('COLLEGES').child(college).child('STUDENT DETAILS').child(uid).child('PERSONAL DETAILS').set(data)
    database.child("users").child(uid).child("details").set(data)
    database.child('COLLEGES').child('REGISTERED').child(uid).set(True)
    return render(request, "alumlogin.html")


def postcollsearch(request):
    uid = request.POST.get('uid')
    passout = request.POST.get('passout')
    name = request.POST.get('sname')
    branch = request.POST.get('branch')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    college = database.child('uid').child(uid).get().val()
    keys = database.child('COLLEGES').child(college).child('STUDENT DETAILS').shallow().get().val()
    flag = 0
    for i in keys:
        if database.child('COLLEGES').child(college).child('STUDENT DETAILS').child(i).child('PERSONAL DETAILS').child(
                'email').get().val() == email and database.child('COLLEGES').child(college).child(
                'STUDENT DETAILS').child(i).child('PERSONAL DETAILS').child('name').get().val().lower() == name.lower():
            print("got you mmffffff")
            flag = 1
            break
    print("flag", flag)
    print("i am here", uid, email)

    return redirect('/')


def postclglogin(request):
    email = request.POST.get('uname')
    password = request.POST.get('psw')
    try:
        user = authe.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid Credentials"
        print("I am in here")
        return render(request, "clglogin.html", {"messg": message})
    clguid = user['localId']
    print(clguid)
    return render(request, 'collsearch.html', {'uid': clguid})
