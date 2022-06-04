import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from urllib.request import urlopen, Request

from .models import Choice, Question

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
        with open('media/image-' + str(n) + '.jpg', "wb") as f:
            f.write(response.read())
        time.sleep(1)

    return HttpResponse("Tu ściągnęłam 5 zdjęć")
