from rest_framework.views import APIView
from quize.serializers import QuizeSerializer
from quize.models import Quize
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

# Create your views here.


class QuizeView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Quize.objects.all()
        serializer = QuizeSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = QuizeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response(data = serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)