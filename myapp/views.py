from django.shortcuts import render
import urllib.request
from bs4 import BeautifulSoup
import re
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ImageLinks
import urllib.request

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def download(request):
    counter = 0
    ImageLinks.objects.all().delete()
    with urllib.request.urlopen(request.POST['pk']) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

    for links in soup.findAll('a', href = re.compile('.jpg')):
        counter += 1
        img = ImageLinks()
        img.imageLocation = links.get('href')
        img.save()

    
    return JsonResponse({"imageCount": counter})

@csrf_exempt
def downloadingImage(request):
    try:
        img = ImageLinks.objects.all().first()
        urllib.request.urlretrieve(img.imageLocation, str(img.id) + ".jpg")
        ImageLinks.objects.all().first().delete()
        return JsonResponse({'download':'success'})
    except:
        return JsonResponse({'download':'fail'})