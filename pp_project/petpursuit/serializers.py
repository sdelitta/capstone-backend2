from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, Canine, Feline, State, Feline, Shelter, UserFelines, UserCanines


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    
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
       fields = ('id','email','first_name','last_name','username','password', 'canines', 'felines')
       extra_kwargs = {'write_only': True}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    #    fields = ('__all__')
    #    extra_fields = ('canines', 'felines')

class CanineSerializer(serializers.ModelSerializer):
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
       fields = ('id', 'dogName', 'breed', 'age', 'photo_url', 'userCanine', 'user', 'shelter')
    #    fields = ('__all__')
    #    extra_fields = ('User', 'Shelter')

class FelineSerializer(serializers.ModelSerializer):
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
       fields = ('id', 'catName', 'breed', 'age', 'photo_url', 'userFeline', 'user', 'shelter')
    #    fields = ('__all__')
    #    extra_fields = ('User', 'Shelter')


class ShelterSerializer(serializers.ModelSerializer):
    state = serializers.HyperlinkedRelatedField(
        view_name='StateDetail',
        many=False,
        read_only=True
    )
    canines = CanineSerializer(
        # view_name='CanineDetail',
        many=True,
        read_only=True
    )
    felines = FelineSerializer(
        # view_name='FelineDetail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Shelter
       fields = ('id', 'shelterName', 'website', 'state', 'canines', 'felines')
    #    fields = ('__all__')
    #    extra_fields = ('State')

class StateSerializer(serializers.ModelSerializer):
    shelters = ShelterSerializer(
        # view_name='ShelterDetail',
        many=True,
        read_only=True,
    )

    class Meta:
       model = State
       fields = ('id','stateName', 'shelters')

class UserFelinesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, source='user_id')
    feline = FelineSerializer(read_only=True, source='feline_id')

    class Meta:
       model = UserFelines
       fields = ('users', 'felines')
    #    fields = ('__all__')
    #    extra_fields = ('user', 'feline')

class UserCaninesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, source='user_id')
    canine = CanineSerializer(read_only=True, source='canine_id')

    class Meta:
       model = UserCanines
       fields = ('users', 'canines')
    #    fields = ('__all__')
    #    extra_fields = ('user', 'canine')