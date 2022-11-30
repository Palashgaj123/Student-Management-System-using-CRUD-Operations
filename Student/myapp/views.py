from cmath import pi
from django.shortcuts import render,HttpResponseRedirect
from  .forms import student, student1
from .models import stud_data1
from .models import stud_login
# Create your views here.

def fun(request):
    if request.method=='POST':
        hm=student(request.POST)
        if hm.is_valid():
            p_cd=hm.cleaned_data['RollNo']
            p_nm=hm.cleaned_data['Name']
            p_em=hm.cleaned_data['Email']
            p_ad=hm.cleaned_data['Department']
            p_dm=hm.cleaned_data['MobileNo']
            reg=stud_data1(RollNo=p_cd,Name=p_nm,Email=p_em,Department=p_ad,MobileNo=p_dm)
            reg.save()
            hm=student()
    else:
        hm=student()
    data=stud_data1.objects.all()
    return render(request,'home.html',{'form':hm,'data':data})

def log(request):
    if request.method=='POST':
        pm=student1(request.POST)
    if pm.is_valid():
            p_cd=pm.cleaned_data['Email']
            p_nm=pm.cleaned_data['Password']
            reg=stud_login(Email=p_cd,Password=p_nm)
            reg.save()
            pm=student1()
    else:
        pm=student1()
    data=stud_data1.objects.all()
    return render(request,'login.html',{'form':pm,'data':data})


def update_data(request, id):
    if request.method == 'POST':
        pi = stud_data1.objects.get(pk=id)
        fm = student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=stud_data1.objects.get(pk=id)
        fm = student(instance=pi)

    return render(request, 'updatestudent.html',{'form':fm})
     
def delete_data(request, id):
    if request.method == 'POST':
        pi = stud_data1.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

