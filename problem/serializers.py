from rest_framework import serializers

from problem.models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', )

class ProblemSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Problem
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        action = self.context.get('account')
        if action == 'list':
            representation['replies'] = instance.replies.count()
        elif action == 'retrieve':
            representation['images'] = ImageSerializer(instance.images.all(), many=True).data
            # representation['replies'] =
        return representation


    def create(self, validated_data):
        request = self.context.get('request')
        image_data = request.FILES
        problem = Problem.objects.create(author=request.user, **validated_data)
        for image in image_data.getlist('image'):
            Image.objects.create(image=image, problem=problem)
        return problem


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Reply
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        reply = Reply.objects.create(author=request.user, **validated_data)
        return reply

#TODO: Коментарии и сериализаторы
#TODO: IsAuthorPermission
#TODO: Добавить PermissionMixin в problem.views
#TODO: Закончить email.html добавить туда ссылку
#TODO: Swagger
#TODO: Celery
#TODO: Model Signals
#TODO: Восстонавление пароля





















