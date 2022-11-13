from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    username:str
    education:str
    interest:str
    experience:str
