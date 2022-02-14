from rest_framework.viewsets import ModelViewSet

from problem.models import Problem, Reply
from problem.serializers import ProblemSerializer, ReplySerializer


# class PermissionMixin:


class ProblemViewSet(ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
