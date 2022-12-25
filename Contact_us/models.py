from django.db import models


# Create your models here.


class Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F" person : {self.email} message : {self.text[:30]} "
