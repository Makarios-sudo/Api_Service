from rest_framework import serializers, viewsets
from accounts.models import Profile
from projects.models import Lecture


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LectureSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many = False)

    class Meta:
        model = Lecture
        fields = "__all__"


