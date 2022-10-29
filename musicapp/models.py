from tkinter import CASCADE
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.Charfield(max_length=225)
    last_name = models.Charfield(max_length=225)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Song(models.Model):
    title = models.Charfield(max_length=225)
    date_released = models.Datefield()
    likes = models.Integerfield()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

class Lyrics(models.Model):
    content = models.TextField(max_length = 1000)
    Song_id = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        if len(self.content) > 50:
          return f"{self.content[0:50]}..."
        else:  
          return f"{self.content}"

