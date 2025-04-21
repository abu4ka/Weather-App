from django.db import models

class RecentCity(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str__(self):
        return self.name