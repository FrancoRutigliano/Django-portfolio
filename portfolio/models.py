from django.db import models
from django.db.models.fields import CharField, URLField, TextField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=200)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
