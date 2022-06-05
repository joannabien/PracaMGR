from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Image(models.Model):
    file_name = models.CharField(max_length=200)

class Vote(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    vote = models.BooleanField()
    user = models.CharField(max_length=200) 

