from django.shortcuts import render

# Create your views here.

def getData(request):
    return render(request,'form.html')

def predict(request):
    return render(request,'result.html')