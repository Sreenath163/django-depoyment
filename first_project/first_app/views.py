from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Employee,Department,Student
from . import forms
# Create your views here.
def index(request):
    return HttpResponse("Hi... I am in index1")

def index2(request):
    return HttpResponse("Hi... I am in index2")

def index3(request):
    my_dict = {'insert_me':"Hello I am in index3"}
    return render(request,'first_app/first_app_index3.html',context=my_dict)

def index4(request):
    my_local = {'insert_me': "Hello I am in index 4"}
    return render(request,'first_app/first_app_index4.html',context=my_local)

def index5(request):
    emp_list = Employee.objects.order_by("empname")
    my_dict = {'access_records':emp_list}
    return render(request,'first_app/first_app_index5.html',context=my_dict)

def index6(request):
    form = forms.MyFormName
    if request.method == 'POST':
        form = forms.MyFormName(request.POST)
        if form.is_valid():
            print("Validation success")
    return render(request,'first_app/first_app_index6.html',{'myform':form})

def index7(request):
    form = forms.MyAdvanceForm
    if request.method == 'POST':
        form = forms.MyAdvanceForm(request.POST)
        if form.is_valid():
            print("Validation success")
    return render(request,'first_app/first_app_index7.html',{'myform':form})

def index8(request):
    form = forms.StudentForm
    if request.method == "POST":
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form")
    return render(request,'first_app/first_app_index8.html',{'form':form})
