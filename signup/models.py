from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAgreement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    terms = models.BooleanField(default=False)
    agreed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Agreed: {self.terms}"