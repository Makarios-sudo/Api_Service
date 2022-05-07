from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import LectureSerializer, ProfileSerializer
from projects.models import Lecture
from accounts.models import Profile

class Lecture_ViewSet(viewsets.ViewSet):
    def list(self, request):
        lectures = Lecture.objects.all()
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = LectureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        lecture = Lecture.objects.get(id=pk)
        serializer = LectureSerializer(lecture)
        return Response(serializer.data)

    def update(self, request, pk=None):
        lecture = Lecture.objects.get(id=pk)
        serializer = LectureSerializer(instance=lecture, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        lecture = Lecture.objects.get(id=pk)
        lecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Profile_ViewSet(viewsets.ViewSet):
    def list(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        profile =Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


    def update(self, request, pk=None):
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(instance=profile, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


