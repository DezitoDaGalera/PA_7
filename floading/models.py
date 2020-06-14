from django.db import models

# Create your models here.
class endereco(models.Model):
    Name= models.CharField(max_length=50)
    Value = models.CharField(max_length=50)

    def __str__(self):
        return self.Name +" "+ self.Value
