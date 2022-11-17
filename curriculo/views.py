
from django.shortcuts import render


def index(request):
    url = 'http://ec2-18-219-40-14.us-east-2.compute.amazonaws.com:8000/certificados/'
    username = 'consumo'
    password = 'certificados'
    #response = requests.get(url=url, auth=(username, password))
    #cursos = response.json()

    # print(cursos)
    # print(type(cursos))

    return render(request, 'curriculo/index.html')
