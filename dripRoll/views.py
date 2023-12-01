# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('HomePage')
    return render(request, 'home.html')