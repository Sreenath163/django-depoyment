from django.shortcuts import render

# Create your views here.
def base(request):
    my_dict = {'title':"Operationss"}
    return render(request,'third_app/base.html',context=my_dict)

def scm(request):
    my_dict = {'title':"SCM"}
    return render(request,'third_app/scm.html',context=my_dict)

def dba(request):
    my_dict = {'title':"DBA",'text':"Hello",'number':100,'extra_text':"hello world"}
    return render(request,'third_app/dba.html',context=my_dict)
