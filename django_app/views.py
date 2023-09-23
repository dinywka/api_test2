from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LessonView, ProductAccess, Product, User
from .serializers import LessonViewSerializer, ProductStatisticsSerializer

@api_view(['GET'])
def lessons_for_user(request):
    user = request.user
    lessons_viewed = LessonView.objects.filter(user=user)
    serializer = LessonViewSerializer(lessons_viewed, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lessons_by_product(request, product_id):
    user = request.user
    if ProductAccess.objects.filter(user=user, product_id=product_id).exists():
        lessons_viewed = LessonView.objects.filter(user=user, lesson__products__id=product_id).order_by('-last_viewed')
        serializer = LessonViewSerializer(lessons_viewed, many=True)
        return Response(serializer.data)
    return Response({"error": "No access to this product or product not found"}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def product_statistics(request):
    products = Product.objects.all()
    serializer = ProductStatisticsSerializer(products, many=True)
    return Response(serializer.data)
