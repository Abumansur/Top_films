from email import feedparser
from statistics import mode
from tkinter import PhotoImage
from unicodedata import category
from django.db import models

class Cartoon(models.Model):

	title       = models.CharField(max_length=100)
	category    = models.TextField(default='genre')
	country		= models.CharField(max_length=30)
	description = models.TextField()
	content     = models.TextField()
	premiere    = models.DateField(default='')
	budget      = models.PositiveIntegerField(default='$')
	fees 		= models.PositiveIntegerField(default='$')
	image 		= models.ImageField(upload_to='images/')

