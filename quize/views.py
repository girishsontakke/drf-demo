from rest_framework.views import APIView
from quize.serializers import QuizeSerializer
from quize.models import Quize
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class QuizeView(APIView):
    def get(self, request):
        queryset = Quize.objects.all()
        serializer = QuizeSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)