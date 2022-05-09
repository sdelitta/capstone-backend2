from rest_framework import serializers
from .models import User, Canine, Feline, State, Feline, UserFelines, UserCanines


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
    class Meta:
       model = User
       fields = ('__all__')
       extra_fields = ('Canine', 'Feline')

class CanineSerializer(serializers.HyperLinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
    view_name='user_detail',
    many=True,
    read_only=True
    )
    shelters = serializers.HyperlinkedRelatedField(
    view_name='shelter_detail',
    many=True,
    read_only=True
    )

    class Meta:
       model = Canine
       fields = ('__all__')
       extra_fields = ('User', 'Shelter')

class FelineSerializer(serializers.HyperLinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )
    shelters = serializers.HyperlinkedRelatedField(
        view_name='shelter_detail',
        many=True,
        read_only=True
    )

    class Meta:
       model = Feline
       fields = ('__all__')
       extra_fields = ('User', 'Shelter')

class StateSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
       model = State
       fields = ('__all__')

class ShelterSerializer(serializers.HyperLinkedModelSerializer):
    states = serializers.HyperlinkedRelatedField(
        view_name='state_detail',
        many=True,
        read_only=True
    )

    class Meta:
       model = State
       fields = ('__all__')
       extra_fields = ('State')

class UserFelinesSerializer(serializers.HyperLinkedModelSerializer):
    user = UserSerializer(read_only=True, source='user_id')
    feline = FelineSerializer(read_only=True, source='feline_id')

    class Meta:
       model = UserFelines
       fields = ('__all__')
       extra_fields = ('user', 'feline')

class UserCaninesSerializer(serializers.HyperLinkedModelSerializer):
    user = UserSerializer(read_only=True, source='user_id')
    canine = CanineSerializer(read_only=True, source='canine_id')

    class Meta:
       model = UserCanines
       fields = ('__all__')
       extra_fields = ('user', 'canine')