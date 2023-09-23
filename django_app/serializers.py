from django.db.models import Sum
from rest_framework import serializers
from .models import LessonView, Product, Lesson, User

class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ['id', 'view_time', 'status', 'user', 'lesson', 'last_viewed']

class ProductStatisticsSerializer(serializers.ModelSerializer):
    total_lessons_watched = serializers.SerializerMethodField()
    total_view_time = serializers.SerializerMethodField()
    total_students = serializers.SerializerMethodField()
    purchase_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_lessons_watched', 'total_view_time', 'total_students', 'purchase_percentage']

    def get_total_lessons_watched(self, obj):
        return LessonView.objects.filter(lesson__products=obj).count()

    def get_total_view_time(self, obj):
        return LessonView.objects.filter(lesson__products=obj).aggregate(Sum('view_time'))['view_time__sum']

    def get_total_students(self, obj):
        return obj.productaccess_set.count()

    def get_purchase_percentage(self, obj):
        total_users = User.objects.count()
        product_users = obj.productaccess_set.count()
        return (product_users / total_users) * 100
