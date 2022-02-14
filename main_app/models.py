from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=500, default="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png")
    current_city = models.CharField(max_length=100, default="Planet Earth")
    bio = models.TextField(max_length=300, default="I love to travel and meet new people.")
    created_at = models.DateTimeField(auto_now_add=True)

class City(models.Model):
    name = models.CharField(max_length=300)
    img = models.CharField(max_length=500)
    country = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
