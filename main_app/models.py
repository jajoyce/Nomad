from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=300)
    img = models.CharField(max_length=500)
    country = models.CharField(max_length=300)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=500, default="https://eitrawmaterials.eu/wp-content/uploads/2016/09/person-icon.png")
    current_city = models.ForeignKey(City, default=1, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, default="I love to travel and meet new people.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        ordering = ['created_at']

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.CharField(max_length=500, default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wysetc.org%2Fwp-content%2Fuploads%2Fsites%2F19%2F2018%2F07%2FAdobeStock_152013093.jpeg&f=1&nofb=1")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on post {self.post.id}"

