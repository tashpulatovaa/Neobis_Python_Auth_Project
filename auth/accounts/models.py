from django.db import models
import uuid
# Create your models here.

class EmailConfirmation(models.Model):
    email = models.EmailField(unique=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email