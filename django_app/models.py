from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_products')

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_in_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, through='ProductLesson')

class ProductLesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time = models.IntegerField()
    status = models.BooleanField()
    last_viewed = models.DateTimeField(auto_now=True)
