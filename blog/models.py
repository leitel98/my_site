from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField()
  id = models.BigAutoField(primary_key=True)
  
  def full_name(self):
        return f"{self.first_name} {self.last_name}"
  
  def __str__(self):
    return self.full_name()
  
  
class Tag(models.Model):
  caption = models.CharField(max_length=20)
  id = models.BigAutoField(primary_key=True)
  
  def __str__(self):
     return self.caption
  
  
class Post(models.Model):
  id = models.BigAutoField(primary_key=True)
  title = models.CharField(max_length=150)
  excerpt = models.CharField(max_length=200)
  image_name = models.CharField(max_length=100)
  date = models.DateField(auto_now=True)
  slug = models.SlugField(unique=True, db_index=True)
  content = models.TextField(validators=[MinLengthValidator(10)])
  author = models.ForeignKey(Author, related_name="posts", on_delete=models.SET_NULL, null=True)
  caption = models.ManyToManyField(Tag)
  
  def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])
  
  def __str__(self):
    return f"{self.title}"