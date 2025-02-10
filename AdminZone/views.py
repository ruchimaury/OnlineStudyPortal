from django.shortcuts import render ,HttpResponse
from general .models import contactModel,myregModel,SigninModel
# Create your views here.
def dashboard(request):
    if(request.session.has_key("aid")):
      return render(request,"dashboard.html")
    else:
        return HttpResponse("<script>alert('Login First then Goto NextZone');window.location.href='/Signin'</script>")

def AddMaterial(request):
    if (request.session.has_key("aid")):
        return render(request,"AddMaterial.html")
    else:
        return HttpResponse("<script>alert('Login First then Goto NextZone');window.location.href='/Signin'</script>")


def AddCourses(request):
    if (request.session.has_key("aid")):
        return render(request, "AddCourses.html")
    else:
        return HttpResponse("<script>alert('Login First then Goto NextZone');window.location.href='/Signin'</script>")


def Management(request):
    if (request.session.has_key("aid")):
        return render(request, "Management.html")
    else:
        return HttpResponse("<script>alert('Login First then Goto NextZone');window.location.href='/Signin'</script>")


def Logout(request):
    del request.session["aid"]
    return HttpResponse("<script>alert('Logout');window.location.href='/Signin'</script>")


def ViewC(request):
    return render(request,"ViewC.html")

def Mts(request):
    return render(request,"Mts.html")

def User(request):
    return render(request,"User.html")

def Contact(request):
    return render(request,"Contact.html")


def ContactData(request):
    return render(request,"Contact.html")




def loginData(request):
    if request.method == 'POST':
        aid = request.POST.get("aid")
        passwd = request.POST.get("passwd")
    try:
        lg = SigninModel.objects.get(aid=aid)
        if lg.aid == aid and lg.passwd == passwd:
            request.session["aid"] = aid  # set the session values
            return HttpResponse(
                "<script>alert('Thanks welcome to Our Next Zone ');window.location.href='/dashboard'</script>")
        else:
            return HttpResponse(
                "<script>alert('Inavlid userid Or Password');window.location.href='/login'</script>")

    except SigninModel.DoesNotExist:
        return HttpResponse(
            "<script>alert('Inavlid userid Or Password');window.location.href='/login'</script>")











