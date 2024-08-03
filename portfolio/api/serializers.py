from django.contrib.auth.models import User
from rest_framework import serializers

from portfolio.models import Profile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'profile_image']
    
    def create(self, validated_data):
        profile_image = validated_data.pop('profile_image', None)
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, profile_image=profile_image)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'summary', 'profile_image']

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile']



class UserProfileUpdateSerializer(serializers.Serializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = fields = ['username', 'first_name', 'last_name', 'profile']
    
    def update(self, instance, validated_date, *args, **kwargs):
        profile_data = validated_date.pop('profile')
        profile_serializer = self.fields['profile']

        for attr, val in validated_date.items():
            setattr(instance, attr, val)
        
        instance.save()

        profile_instance = instance.profile

        profile_serializer.update(profile_instance, profile_data)

        return instance
