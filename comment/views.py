from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsAuthorPermission, IsActive
from rest_framework.permissions import AllowAny


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsActive]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class CommentViewSet(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

