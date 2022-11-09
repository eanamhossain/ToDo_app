from django.db import models
from django.urls import reverse
# Create your models here.

class todo(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    def get_success_url(self):
        return reverse('todo_create', kwargs={'pk': self.object.pk})
    