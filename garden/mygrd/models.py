from django.db import models

# Create your models here.
class aboutinfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    messaage=models.TextField()

class product(models.Model):
    discription=models.TextField()
    upload_photo=models.ImageField(upload_to="product/")