from django.db import models

# Create your models here.

class Status(models.Model):
    
    class Meta: 
        verbose_name = "Status"
        verbose_name_plural = "Status"


    statu = models.CharField('Estado', max_length=100)

    def __str__(self):
        return f"{self.statu}"