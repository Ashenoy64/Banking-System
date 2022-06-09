from atexit import register
import re
from turtle import color
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import context
from django.views.decorators.csrf import csrf_exempt
from myapp.models import usercomplaints,customer,transfer
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from random import randint

def home(request):
    return render(request,"Home.html")

@csrf_exempt
def form(request):
    context={}
    if request.method=="POST" :
        name=request.POST["username"] 
        email=request.POST["email"]
        di=request.POST["id"]
        pwd=request.POST["password"]
        cpwd=request.POST["confirm_password"]
        if cpwd==pwd:
            usr=User.objects.create_user(name,email,pwd)
            usr.save()
            reg=customer(user=usr,contact_number=di)
            reg.save()
            l=User.objects.all().count()
            l=str(l)
            r=randint(1000,9999)
            r=str(r)
            u=transfer(value=1000,gbd="GHB"+l+r,pin=pwd,user=name)
            u.save()
            return render(request,"form.html",{"status":"Registered Successfully"})
        else:
            context["mis"]="Password Mismatch!"
    return render(request,"form.html",context)  

@csrf_exempt
def contact(request):                          #puts the data to the database
    #data=usercomplaints.objects.all()/.order_by(-di)
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        di=request.POST["ID"]
        sub=request.POST["sub"]
        comp=request.POST["msg"]
        data=usercomplaints(name=name,di=di,email=email,sub=sub,comp=comp)
        data.save()
        res="Dear {} Thanks for your feedback".format(name)
        return render(request,"contact.html",{"status":res})

    #return render(request,"contact.html",{"messages":data})
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")    

@csrf_exempt
def user_login(request):
    if request.method=="POST":
        un=request.POST["username"]
        pwd=request.POST["password"]
        
        user=authenticate(username=un,password=pwd)
        if user:
            login(request,user,)
            if user.is_superuser:
               return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/dashboard")   
        else:
            return render(request,"login.html",{"status":"Invalid Username or Password"})
    return render(request,"login.html")

def check_user(request):
    if request.method=="GET":
        un=request.GET["name"]
        check=User.objects.filter(username=un)
        if len(check)==1:
            return HttpResponse("exist")

@login_required
def dashboard(request):
    u=User.objects.get(id=request.user.id)
    user1=transfer.objects.get(user=u.username)
    cust=customer.objects.get(user__id=request.user.id)
    u={}
    u["data"]=user1
    u["customer"]=cust
    return render(request,"userdashboard.html",u)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/home")    

@csrf_exempt
def edit_profile(request):
    context={}
    u=User.objects.get(id=request.user.id)
    user1=transfer.objects.get(user=u.username)
    data= customer.objects.get(user__id=request.user.id)
    context["data"]=user1
    context["data1"]=data
    context["user"]=u
    if request.method=="POST":
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        em=request.POST["email"]
        con=request.POST["contact"]
        age=request.POST["age"]


        usr=User.objects.get(id=request.user.id)
        usr.first_name=fn
        usr.last_name=ln
        usr.email=em
        usr.save()    

        data.contact_number=con
        data.age=age
        context["status"]="Changes saved Succesfully"
    if "image" in request.FILES:
        img=request.FILES["image"]
        data.profie_pic=img
    return render(request,"edit_profile.html",context)    

@csrf_exempt
def change(request):
    context={}
    u=User.objects.get(id=request.user.id)
    user1=transfer.objects.get(user=u.username)
    context["data"]=user1
    if request.method=="POST":
        current_password=request.POST["cpwd"]
        new_password=request.POST["npwd"]

        user=User.objects.get(id=request.user.id)
        un=user.username
        check=user.check_password(current_password)
        if check:
            user.set_password(new_password)
            context["msz"]="Password Changed successfully!"
            user.save()
            u=authenticate(username=un,password=new_password)
            login(request,u)
            a=transfer.objects.get(user=user.username)
            a.pin=new_password
            a.save()
            context["col"]='alert-success'
        else:
            context["msz"]="Incorrect Password!"
            context["col"]='alert-danger'
            

    return render(request,"change.html",context)    

@csrf_exempt
def trans(request):
    t=1
    context={}
    data=transfer.objects.get(user=request.user.username)
    context["data"]=data
    if request.method=="POST":
        u=request.POST["username"]
        g=request.POST["rid"]
        p=request.POST["pwd"]
        v=request.POST["amt"]
        v=int(v)
        try:
            user2=transfer.objects.get(gbd=g)
        except:
            context["Incorrect"]="Invalid ID"
            t=0  
        try:
            if user2.user!=u:
               t=0
               context["dont"]="Username And ID doesnt match" 
        except:
            pass            
        u=User.objects.get(id=request.user.id)
        user1=transfer.objects.get(user=u.username)
        if user1.pin != p:
            t=0
            context["incorrect"]="Pin is Incorrect"
        if user1.value<v:
            t=0
            context["F"]="Insufficient amount"

        if t:
            user2.value+=v
            user1.value-=v
            context["transaction"]="Transaction Succesfull"    
            user1.save()
            user2.save()
            context["data"].value-=v





    return render(request,"transaction.html",context)