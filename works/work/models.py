from django.db import models

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    thumb = models.ImageField(default='default.png',blank=True)
    rar_file = models.FileField(upload_to='media/',default='default.rar',blank=True)




    def __str__(self):
        return self.title