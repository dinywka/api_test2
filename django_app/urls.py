from django.urls import path
from . import views

urlpatterns = [
    path('user/lessons/', views.lessons_for_user, name='user-lessons'),
    path('products/<int:product_id>/lessons/', views.lessons_by_product, name='product-lessons'),
    path('products/statistics/', views.product_statistics, name='product-statistics')
]
