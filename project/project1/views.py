from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import user_passes_test,login_required

def index(request):
    return render(request,'index.html')
