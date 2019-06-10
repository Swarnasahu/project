from django.shortcuts import render
from.models import RegistrationData
from.forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse
def home(request):
    return render (request,'reglogin.html')
def registration(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            firstname=request.POST.get("firstname",'')
            lastname=request.POST.get("lastname",'')
            username = request.POST.get("username", '')
            email = request.POST.get("email", '')
            number = request.POST.get("number", '')
            password1= request.POST.get("password1", '')
            password2 = request.POST.get("password2", '')
            data=RegistrationData(
                firstname=firstname,
                lastname=lastname,
                username=username,
                email=email,
                number=number,
                password1=password1,
                password2=password2)
            data.save()
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
    else:
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
def login(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password1=request.POST.get('password1','')
            user=RegistrationData.objects.filter(username=username)
            pwd=RegistrationData.objects.filter(password1=password1)
            if user and pwd:
                return HttpResponse('valid details')
            else:
                return HttpResponse('Invalid details')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'form':lform})
