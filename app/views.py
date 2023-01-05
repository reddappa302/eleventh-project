from django.shortcuts import render

# Create your views here.
def operational(request):
    d={'a':10,'b':20}
    return render(request,'operational.html',d)

def operational1(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'operational1.html',d)    
