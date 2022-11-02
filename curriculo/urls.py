from django.urls import path
from curriculo.views import index

urlpatterns = [
    path('', index, name='index'),
]