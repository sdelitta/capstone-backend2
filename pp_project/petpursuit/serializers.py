from rest_framework import serializers
from .models import User, Canine, Feline, State, Feline, Shelter, UserFelines, UserCanines


class UserSerializer(serializers.HyperlinkedModelSerializer):
    canines = serializers.HyperlinkedRelatedField(
        view_name='CanineDetail',
        many=True,
        read_only=True
    )
    felines = serializers.HyperlinkedRelatedField(
        view_name='FelineDetail',
        many=True,
        read_only=True
    )
    class Meta:
       model = User
       fields = ('userName', 'email', 'password', 'canines', 'felines')
    #    fields = ('__all__')
    #    extra_fields = ('canines', 'felines')

class CanineSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
    view_name='UserDetail',
    many=True,
    read_only=True
    )
    shelter = serializers.HyperlinkedRelatedField(
    view_name='ShelterDetail',
    many=False,
    read_only=True
    )

    class Meta:
       model = Canine
       fields = ('dogName', 'breed', 'age', 'photo_url', 'userCanine', 'user', 'shelter')
    #    fields = ('__all__')
    #    extra_fields = ('User', 'Shelter')

class FelineSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='UserDetail',
        many=True,
        read_only=True
    )
    shelter = serializers.HyperlinkedRelatedField(
        view_name='ShelterDetail',
        many=False,
        read_only=True
    )

    class Meta:
       model = Feline
       fields = ('catName', 'breed', 'age', 'photo_url', 'userFeline', 'user', 'shelter')
    #    fields = ('__all__')
    #    extra_fields = ('User', 'Shelter')

class StateSerializer(serializers.ModelSerializer):
    shelters = serializers.HyperlinkedRelatedField(
        view_name='ShelterDetail',
        many=True,
        read_only=True
    )

    class Meta:
       model = State
       fields = ('__all__')

class ShelterSerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.HyperlinkedRelatedField(
        view_name='StateDetail',
        many=False,
        read_only=True
    )
    canines = serializers.HyperlinkedRelatedField(
        view_name='CanineDetail',
        many=True,
        read_only=True
    )
    felines = serializers.HyperlinkedRelatedField(
        view_name='FelineDetail',
        many=True,
        read_only=True
    )

    class Meta:
       model = Shelter
       fields = ('shelterName', 'website', 'state', 'canines', 'felines')
    #    fields = ('__all__')
    #    extra_fields = ('State')

class UserFelinesSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True, source='user_id')
    feline = FelineSerializer(read_only=True, source='feline_id')

    class Meta:
       model = UserFelines
       fields = ('users', 'felines')
    #    fields = ('__all__')
    #    extra_fields = ('user', 'feline')

class UserCaninesSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True, source='user_id')
    canine = CanineSerializer(read_only=True, source='canine_id')

    class Meta:
       model = UserCanines
       fields = ('users', 'canines')
    #    fields = ('__all__')
    #    extra_fields = ('user', 'canine')