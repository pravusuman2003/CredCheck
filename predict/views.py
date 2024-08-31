from django.shortcuts import render

# Create your views here.

def getData(request):
    return render(request,'get_data.html')