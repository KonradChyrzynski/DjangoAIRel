from django.core import serializers
from django.http import HttpResponse
from .models import Article

# Create your views here.


def getarticles(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


def home_id(request, id):
    return HttpResponse(f"Hello, World! {id}")
