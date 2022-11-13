from django.shortcuts import render

from django.contrib.auth.models import User , auth 

# Create your views here.
def home_new(request):
    name=("ahahah")
    return render(request,'home_new.html',{'name':name})

def register(request):
    
    if request.method=='POST':
        first_name=request.POST['name']
        last_name=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        pwd1=request.POST['pw']
        pwd2=request.POST['cpw']
        if pwd1!=pwd2:
            message=("Password Not Matching!!")
            return render(request,'register.html',{'message':message})
        elif User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            
            message=("Username Already Exists \n Please select different username ")
            return render(request,'register.html',{'message':message})
        else:
            user=User.objects.create_user(username=username,password=pwd1,email=email,first_name=first_name,last_name=last_name)
            user.save();
            return render(request,'page2.html')
    else :
        return render(request,'register.html') 
           
def login(request):
    username=request.POST.get('username')
    password=request.POST.get('pw')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
            auth.login(request,user)
            return render(request,'page2.html')
    else:
            message=("Incorrect Username or Password ")
            return render(request,'login.html',{'message':message}) 
def studenthome(request):
    return render(request,'studenthome.html')
def page2(request):
    return render(request,'page2.html')
def page1(request):
    return render(request,'page1.html')

def logout(request):
    auth.logout(request)
    return render(request,'home_new.html')
def page2(request):
    return render(request,'page2.html')
def personalinfo(request):
    return render(request,'personalinfo.html')
def company(request):
    return render(request,'company.html')
def company2(request):
    return render(request,'company2.html')
def company3(request):
    return render(request,'company3.html')
def company4(request):
    return render(request,'company4.html')
def company5(request):
    return render(request,'company5.html')
def company6(request):
    return render(request,'company6.html')
'''

              
        username=request.GET('username')
        education=request.GET('education')
        interest=request.GET('interest')
        experience=request.GET('experience')
        user=User.objects.create_user(username=username,education=education,interest=interest,experience=experience)
        user.save();

'''
    
  