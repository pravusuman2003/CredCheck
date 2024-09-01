from django.shortcuts import render

# Create your views here.

def getData(request):
    return render(request,'form.html')