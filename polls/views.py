from email.mime import image
from pickle import TRUE
import random
import secrets
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.urls import reverse
from urllib.request import urlopen, Request

from .models import Image, Question, Vote

def detail(request, question_id):
    return HttpResponse("Czy ta osoba jest atrakcyjna? %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    

def download(request):

    ## konfiguruje adres URL obrazów
    url = 'https://thispersondoesnotexist.com/image'

    x = range(5)
    for n in x:
        requestImage = Request(url + '?' + str(n), headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(requestImage)
        fileName = 'image-' + secrets.token_hex(nbytes=8) + '.jpg'
        with open('polls/static/polls/media/' + fileName, "wb") as f:
            f.write(response.read())
        img = Image (file_name= fileName)
        img.save()
        time.sleep(1)

    return HttpResponse("Tu ściągnęłam 5 zdjęć")

def show(request):
    if not request.session.session_key:
            request.session.create()
    session_key = request.session.session_key      

    images = Image.objects.all()
    image = random.choice(images)
    #image = Image.objects.get(items)

    vote = Vote(vote = True, image = image, user = session_key )
    vote.save() #to jest do poprawienia

    
    

    return render(request, 'polls/show.html', {'image': image})