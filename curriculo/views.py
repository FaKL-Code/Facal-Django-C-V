from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    url = 'http://127.0.0.1:8000/certificados'
    username = 'consumo'
    password = 'certificados'
    response = requests.get(url=url, auth=(username, password))
    cursos = response.json()
    
    print(cursos)
    print(type(cursos))
    
    return render(request, 'curriculo/index.html')
