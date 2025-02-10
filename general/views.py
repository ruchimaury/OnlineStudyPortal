import re
from _ast import mod

from django.shortcuts import render,HttpResponse
from general.models import SigninModel,myregModel,contactModel
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def onlinestudyzone(request):
    return render(request,'onlinestudyzone.html')

def index(request):
    return render(request,'onlinestudyzone.html')


def Materials(request):
    return render(request,"Materials.html")

def AboutUs(request):
    return render(request,"AboutUs.html")

def ContactUs(request):
    return render(request,"ContactUs.html")

def MyProfile(request):
    return render(request, "Myprofile.html")

def Signin(request):
    return render(request,"Signin.html")

def SignUp(request):
    return render(request,"SignUp.html")

def SigninData(request):
    if request.method=="POST":
        aid=request.POST.get("aid")
        passwd=request.POST.get("passwd")
    try:
        lg=SigninModel.objects.get(aid=aid)
        if(lg.aid==aid and lg.passwd==passwd):
            request.session["aid"] = aid
            return HttpResponse("<script>alert('Welcome');window.location.href='/dashboard'</script>")
        else:
            return HttpResponse("<script>alert('Invailid userid or password');window.location.href='/Signin'</script>")


    except SigninModel.DoesNotExist:
        return HttpResponse("<script>alert('Invailid userid or password');window.location.href='/Signin'</script>")

def contactData(request):
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            mob = request.POST.get("mob")
            msg = request.POST.get("msg")
        try:
            '''subject = 'Welcome to O-Study Zone'
            message = f'Hi {name} thanks for contact.As soon as we contact you'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            email_from(subject, message, email_from, recipient_list)
            '''
            data = contactModel(name=name,email=email,mob=mob,msg=msg)
            data.save()
            return HttpResponse("<script>alert('thanks for contact');window,location.href='/Contactus'</script>")

        except:
            return HttpResponse("<script>alert('record not submited');window,location.href='/Contactus'</script>")

def regData(request):
    Name = request.POST.get('name')
    course=request.POST.get('course')
    gender=request.POST.get('gender')

    mob = request.POST.get('mob')
    email = request.POST.get('email')
    captcha = request.POST.get('captcha')

    passwd=request.POST.get('passwd')
    city=request.POST.get('city')
    add = request.POST.get('add')
    hdn = request.POST.get('hdn')
    if(hdn == captcha):
        data = myregModel(name=Name,course=course,mob=mob,passwd=passwd,email=email,add=add,city=city,gender=gender)
        data.save()
        return HttpResponse("<script>alert('Thanks for Registration');window.location.href='/signup'</script>")

    else:
        return HttpResponse("<script>alert('invalid captcha code');window.location.href='/signup'</script>")
