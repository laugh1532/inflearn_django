from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()

    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)
