from django.shortcuts import render,redirect
from .models import *
from .blockchain import *
import random
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    context = {}
    try:
        
        if request.user.is_authenticated == True:
            profile = Profile.objects.get(user=request.user)
            context['profile'] = profile
            # print("Test",profile.roll)
        else:
            context['profile']=[]
    except:
        print("Somthing went wrong")
    return render(request,'index.html',context)

def getData(request,fld):
    return request.POST.get(fld,'')

@login_required()
def ins(request):

    if request.method == 'POST':
        name = getData(request, 'ne')
        aadhar = getData(request, 'aadhar')
        num = getData(request, 'aano')
        email = getData(request, 'email')
        dob = getData(request, 'dob')
        father = getData(request, 'fname')
        mother = getData(request, 'mname')
        addres = getData(request, 'as')
        stus = getData(request, 'MS')
        spous = getData(request, 'SPOUSE')
        qulifi = getData(request, 'QUALIFICATION')
        pob = getData(request, 'PBIRTH')
        pan = getData(request, 'pan')
        occ = getData(request, 'ems')
        ai = getData(request, 'AINCOME')
        Ename = getData(request, 'EMPLOYEENAME')
        Eser = getData(request, 'yos')

        datas = Insure.objects.all()
        l = len(datas)

        model = {
            'id':random.randint(0, 99999),
            'adhar':aadhar,
            'name':name
        }

        if l == 0:
            block = Block('Initial hash', model)    
            new_hash = block.new_hash
        else:
            
            last_data = datas[l-1]
            previous_hash = last_data.new_hash
            block = Block(previous_hash, model)    
            new_hash = block.new_hash

            # BlockChain = Block(previous_hash, model)
        obj = Insure(
                user=request.user,
                name=name,
                adhar=aadhar,
                adhar_mobile=num,
                email=email,
                dob=dob,
                father_name=father,    
                mother_name=mother,
                address=addres,
                status=stus,
                spouse=spous,
                qulification=qulifi,
                pob=pob,
                pan=pan,
                occupation=occ,
                AIncome=ai,
                Employer=Ename,
                service=Eser,
                new_hash=new_hash
            )
        obj.save()

        messages.success(request, "Data created!! New hash value Created "+ str(new_hash)+".")
        return redirect('index')

    return render(request, 'ins.html',{})

@login_required()
def Dashboard(request):
    context = {}
    profile = Profile.objects.filter(user=request.user)
    
    if len(profile)!=0:
        profile = profile[0]
        context['profile'] = profile
        if profile.roll == 'insure':
            context['datas'] = Insure.objects.filter(user=request.user)
        else:
            context['provider'] = Provider.objects.filter(user=request.user)
            context['datas'] = Insure.objects.all()
    else:
        context['datas'] = []
        context['profile'] = []
        context['provider'] = []

    return render(request, 'dash.html',context)

def UserLogin(request):
    print("CAlled")
    if request.method == 'POST':
        username = getData(request, 'username')
        password = getData(request, 'password')

        user = authenticate(request,username=username,password=password)


        if user is not None:
            login(request, user)
            messages.success(request, 'Successfull Login!!')
            
            return redirect('index')
            

        else:
            messages.success(request, 'Invalid  Credentials')

    return render(request,'login.html',{})

def Register(request):
    print("CAlled") 
    if request.method == "POST":
        username = getData(request, 'username')
        Email = getData(request, 'email')
        FirstName = getData(request, 'firstname')
        LastName = getData(request, 'lastname')
        roll = getData(request, 'roll')
        NewPassword = getData(request, 'passwd')
        ConfirmPassword = getData(request, 'cpassword')

        if NewPassword == ConfirmPassword:
            obj = User.objects.create_user(
                username=username,
                email=Email,
                first_name=FirstName,
                last_name=LastName,
                password=ConfirmPassword
            )
            print(ConfirmPassword,NewPassword)
            obj.save()
            print(obj)
            pro = Profile(user=obj,roll=roll,email=Email,name=username)
            pro.save()
            user = authenticate(request,username=username,password=NewPassword)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfull Login!!')
                return redirect('index')
            else:
                messages.success(request, 'Login Fail !!')
            # messages.success(request, 'Login Fail !!')


        else:
            messages.success(request, 'Invalid  Credentials!!')
            
    return render(request,'login.html',{})

@login_required()
def Logout(request):
    logout(request)
    messages.success(request, 'Loged Out')

    return redirect('index')

def provider(request):

    if request.method == 'POST':
        name = getData(request, 'name')
        hospital = getData(request, 'hospital')
        address = getData(request, 'address')
        contry = getData(request, 'country')
        state = getData(request, 'state')
        city = getData(request, 'city')

        pincode = getData(request, 'pincode')
        email = getData(request, 'email')

        ENT = request.FILES.get('ENT')
        ED= request.FILES.get('ED')
        AT = request.FILES.get('AT')
        HI = request.FILES.get('HI')
        
        datas = Provider.objects.all()
        l = len(datas)

        model = {
            'id':random.randint(0, 99999),
            'adhar':hospital,
            'name':name
        }

        if l == 0:
            block = Block('Initial hash', model)    
            new_hash = block.new_hash
        else:
            
            last_data = datas[l-1]
            previous_hash = last_data.new_hash
            block = Block(previous_hash, model)    
            new_hash = block.new_hash

        # print(ENT,ED,AT,HI,email,address)
        obj = Provider(
            user=request.user,
            service=name,
            hospital=hospital,
            address=address,
            country=contry,
            state=state,
            city=city,
            pincode=pincode,
            email=email,

            ENT = ENT,
            ED=ED,
            AT=AT,
            HI=HI,

            new_hash=new_hash
        )
        obj.save()
        messages.success(request, 'Provider Created !!')
        return redirect('dash')

    return render(request,'provider.html',{})