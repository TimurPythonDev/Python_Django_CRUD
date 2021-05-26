from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegisters
from .models import User
# Create your views here.

# Timur Karabayev
# 26.05.2021


#  This is a Functions Update
def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegisters(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegisters(instance=pi)
    return render(request,'update.html', {'form':fm})

# -------------------------------------------------------




# This is a Function Add
def add(request):
    if request.method =='POST':
       fm =  StudentRegisters(request.POST)
       if fm.is_valid():
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email']
           pw = fm.cleaned_data['password']
           reg = User(name=nm,email=em,password=pw)
           reg.save()
           fm = StudentRegisters()

    else:
        fm = StudentRegisters()
    stud = User.objects.all()

    return render(request,'addStudents.html',{'form':fm,'stu':stud})

# --------------------------------------------------------------------


# This is a Deletions Function


def delete_date(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# ------------------------------------------

