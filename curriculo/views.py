from django.test import Client
from django.urls import reverse


def index(request):
    url = 'http://ec2-18-219-40-14.us-east-2.compute.amazonaws.com:8000/certificados/'
    username = 'consumo'
    password = 'certificados'
    #response = requests.get(url=url, auth=(username, password))
    #cursos = response.json()

    # print(cursos)
    # print(type(cursos))

    client = Client(HTTP_HOST="www.example-a.dev")
    view = reverse("index")
    response = client.get(view)
    request.assertEqual(response.status_code, 200)
