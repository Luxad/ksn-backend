from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Post
from .serializers import NewsSerializer


class PostsList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        news_list = Post.objects.all()
        serializer = NewsSerializer(news_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
