from datetime import datetime

from django.shortcuts import HttpResponse, redirect

def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Hello! Its my project")

def time_view(request):
    if request.method == 'GET':
        now_date = datetime.now()
        return HttpResponse(now_date)

def good_by_view(request):
    if request.method =='GET':
        return HttpResponse('Goodby user!')