from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse("khit")
    return render(request, 'hompage.html')

def homepage(request):
    #return HttpResponse("hompage")
    return render(request, 'about.html')
