from django.db import models
import string
import random

class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.CharField(max_length=6, unique=True)
    clicks = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.url_hash:
            self.url_hash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
        super().save(*args, **kwargs)
