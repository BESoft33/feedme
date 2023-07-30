from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from applications.user_handler.models import User

def index(request):
    auth = authenticate(username='9803788148', password='@Yamaraj33')
    return HttpResponse(f"<p>Authentication is: {auth} </p>")
