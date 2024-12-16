from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name','email', 'phone_number', 'password', 'confirm_password']
        read_only_fields = ['id']

    def validate(self, data):
        if data['password'] != data.get('confirm_password'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # remove confirm_password from validated_data
        validated_data.pop('confirm_password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
