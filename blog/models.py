from django.db import models

# Create your models here.


class Blog(models.Model):
    # Title
    title = models.CharField(max_length=60)
    # Publication date
    pub_date = models.DateTimeField()
    # Body
    body = models.TextField()
    # Image
    image = models.ImageField(upload_to='images/')
