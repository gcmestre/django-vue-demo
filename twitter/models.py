from django.db import models

# Create your models here.


class Tweet(models.Model):
    message = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_date) + ' - ' + self.name + ': ' + self.message
