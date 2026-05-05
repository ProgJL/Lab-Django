from django.db import models

# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ("P", "Pendente"),
        ("C", "Concluída"),
    ]

    title = models.CharField(max_length=255)

    description = models.TextField(blank=True)

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="P")

    def __str__(self):
        return self.title
