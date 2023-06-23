from django.db import models

# Create your models here.
class Postdb(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to ='image/')


    def __str__(self):
        return self.title