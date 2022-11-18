from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from posts.models import Post
from posts.permissions import CustomReadOnly
from posts.serializers import PostSerializer, PostCreateSerializer


class ProjectListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


def home(request):
    posts = Post.objects.all() # select * from post;
    return render(request, 'index.html', {'posts': posts})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = ProjectListPagination
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
