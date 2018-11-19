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

    def __str__(self):
        return self.title
    # Return certain portion of thje summary

    def body_summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
