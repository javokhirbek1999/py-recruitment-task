from rest_framework import serializers

from ..models import users


class UserSerializer(serializers.ModelSerializer):
    """Serializer for creating client users"""

    class Meta:
        model = users.User
        fields = ('id', 'email', 'username', 'password', 'is_active', 'date_joined', 'date_updated')
        extra_kwargs = {
            'password': {'write_only': True, 
                         'style': {'input_type': 'password'}},
            'date_joined': {'read_only': True},
            'date_updated': {'read_only': True}
        }
    

class AdminUserSerializer(serializers.ModelSerializer):
    """Serializer for creating admin users"""

    class Meta:
        model = users.User
        fields = ('id', 'email', 'username', 'password', 'is_active', 'date_joined', 'date_updated')
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'date_updated': {'read_only': True}
        }

    
    def create(self, validated_data):
        return self.Meta.model.objects.create_superuser(**validated_data)