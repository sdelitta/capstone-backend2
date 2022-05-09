from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    canines = serializers.HyperlinkedRelatedField(
        view_name='canine_detail',
        many=True,
        read_only=True
    )
    felines = serializers.HyperlinkedRelatedField(
        view_name='feline_detail',
        many=True,
        read_only=True
    )

    user_url = serializers.ModelSerializer.serializer_url_field(
    view_name='user_detail'
    )
    class Meta:
       model = User
       fields = ('id', 'user_url', 'userName', 'email', 'password', 'canines', 'felines')