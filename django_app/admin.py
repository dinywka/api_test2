from django.contrib import admin
from django_app import models

# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.ProductAccess)
admin.site.register(models.Lesson)
admin.site.register(models.ProductLesson)
admin.site.register(models.LessonView)
