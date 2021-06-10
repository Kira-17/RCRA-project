from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import patient,doctor,patientsymptoms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

def indexpage(request):

    return render(request,'index.html')

def signup_patient_page(request):
    if request.method=="POST":
        if request.POST['psw']==request.POST['passwordagain']:
            try:
                user=User.objects.get(username=request.POST['username1'],email=request.POST['email'])
                return render(request,'signup_patient.html',{'error':"username already name taken"})
            except User.DoesNotExist:
                user= User.objects.create_user(username=request.POST['username1'],email=request.POST['email'],password=request.POST['psw'])
                # doc_id=doctor(number_doc=request.POST['number_doc'])
                # doc_id=doc_id.save()
                # patient.doc_id=doc_id
                # patient.save()
                name=request.POST['name']
                surname=request.POST['surname']
                patient_id=request.POST['patient_id']
                address=request.POST['address']
                number=request.POST['number']
                emergency_number=request.POST['emergency_number']
                age=request.POST['age']
                health_condition=request.POST['health_condition']
                gender=request.POST['gender']
                
                alternate_email=request.POST['alternate_email']
                doctorr_id=request.POST['doctorr']
                doctorop=doctor.objects.get(id=doctorr_id)
                #doctorw= doctorop
                new_patient=patient(name=name,surname=surname,patient_id=patient_id,address=address,number=number,emergency_number=emergency_number,age=age,health_condition=health_condition,gender=gender,alternate_email=alternate_email,doctorw=doctorop,user=user)
                new_patient.save()
                messages.success(request,'Account created succesfully')
                auth.login(request,user)
                return HttpResponse("signed up")
        else:
            return render(request,'signup_patient.html',{'error':"password dont match"})
    else:
        return render(request,'signup_patient.html',{'doctors':doctor.objects.all()})

def login_patient_page(request):
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username1'], password=request.POST['psw'])
        if user is not None:
            auth.login(request,user)
            return render(request,'patient_profile.html')
        else:
            return render(request,'login_patient.html',{'error':"invalid"})
    else:
        return render(request,'login_patient.html')



@login_required(login_url='/login_patient/')
def patient_profile_page(request,patient_id):
    # datas=patient.objects.filter(id=patient_id)

    datas= patient.objects.filter(user=request.user)
    print(datas)
    print(datas[0].user.id)
    if request.method=="POST":
        btemp=request.POST.get('btemp')
        sympt1=request.POST.get('sympt1')

        # doctorr_id=request.POST['doctorr']
        # doctorop=doctor.objects.get(id=doctorr_id)
        # patient_fkey=request.user

        # patientop=patient.objects.get(id=datas[0].user.id)
        patient_fkey=request.user.patient
        print("hi")
        savedata=patientsymptoms(btemp=btemp,sympt1=sympt1, patient_fkey=patient_fkey)
        
        savedata.save()
        savedata.history.all()
        return render(request,'patient_profile.html',{'data':datas})
        
        
    else:
        return render(request,'patient_profile.html',{'data':datas})

@login_required(login_url='/login_patient/')
def patient_logout(request):
    logout(request)
    return render(request,'index.html')


# doctor
def signup_doctor_page(request):
    if request.method=="POST":
        if request.POST['pwd']==request.POST['pwdagain']:
            try:
                user_doc=User.objects.get(username=request.POST['username2'],email=request.POST['email_doc'])
                return render(request,'signup_doctor.html',{'error':"username already name taken"})
            except User.DoesNotExist:
                user_doc= User.objects.create_user(username=request.POST['username2'],email=request.POST['email_doc'],password=request.POST['pwd'])
                full_name=request.POST['full_name']
                hospital_name=request.POST['hospital_name']
                number_doc=request.POST['number_doc']
            
                new_doctor=doctor(full_name=full_name,hospital_name=hospital_name,number_doc=number_doc,user_doc=user_doc)
                new_doctor.save()
                messages.success(request,'Account created succesfully')
                auth.login(request,user_doc)
                return HttpResponse("signed up")
        else:
            return render(request,'signup_doctor.html',{'error':"password dont match"})
    else:
        return render(request,'signup_doctor.html')


def login_doctor_page(request):
    if request.method=="POST":
        user_doc=auth.authenticate(username=request.POST['username2'], password=request.POST['pwd'])
        if user_doc is not None:
            auth.login(request,user_doc)
            return render(request,'doctor_profile.html')
        else:
            return render(request,'login_doctor.html',{'error':"invalid"})
    else:
        return render(request,'login_doctor.html')


@login_required(login_url='/login_doctor/')
def doctor_profile_page(request,doctor_id):
    id=doctor_id
    datas= doctor.objects.filter(user_doc=request.user)
    y=patient.objects.filter(doctorw__in=datas)
    z=patientsymptoms.objects.filter(patient_fkey__in=y)
    print(z)
    print(patientsymptoms.history.all())
    x=patientsymptoms.history.all()
    # print(x[0].btemp)

    mylist= zip(y,z)
    # mylist=zip(x,y,z)
    
    context={
        'data':datas,
        'mylists':mylist,
        'hist':x
        
    }
    # context={
    #     'data':datas,
    #     'mylists':mylist,
        
        
    # }
    
    print(z[3].history)
    return render(request,'doctor_profile.html',context)

