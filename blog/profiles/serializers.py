from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image',)
        read_only_fields = ('username',)

    def _get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'


class ProfileSerializerUpdate(serializers.ModelSerializer):
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'image',)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Performs an update on a Profile."""

        # Update Pasword
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        instance.save()

        # Update profile
        profile_data = validated_data

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()

        return instance
