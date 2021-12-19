from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for creating client users"""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'is_active', 'date_joined', 'date_updated')
        extra_kwargs = {
            'password': {'write_only': True, 
                         'style': {'input_type': 'password'}},
            'date_joined': {'read_only': True},
            'date_updated': {'read_only': True}
        }
    
    def update(self, instance, validated_data):
        return self.Meta.model.objects.creaate_user(**validated_data)

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)
    

class AdminUserSerializer(serializers.ModelSerializer):
    """Serializer for creating admin users"""

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'date_joined', 'date_updated')
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'date_updated': {'read_only': True}
        }

    
    def create(self, validated_data):
        return self.Meta.model.objects.create_superuser(**validated_data)