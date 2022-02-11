from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=500, default="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png")
    current_city = models.CharField(max_length=100, default="Planrt Earth")
    created_at = models.DateTimeField(auto_now_add=True)