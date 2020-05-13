from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'second_app/second_app_index.html')

def other(request):
    return render(request,'second_app/second_app_other.html')

def relative(request):
    return render(request,'second_app/second_app_relative.html')
