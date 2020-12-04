from rest_framework import generics, mixins

from core.serializers import PostSerializer
from core.models import Post


# Create your views here.
class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request):
        return self.create(request)


# from django.shortcuts import render
# from django.http import JsonResponse
#
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated

# class PostView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostView(APIView):
#     permission_classes = [
#         IsAuthenticated,
#     ]

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors)
