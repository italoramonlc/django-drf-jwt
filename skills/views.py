from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from core.permissions import IsAdminUserOrRadOnly

from .models import Skill
from .serializers import SkillSerializer


class SkillList(APIView):
    permission_classes = (IsAdminUserOrRadOnly,)
    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillDetail(APIView):
    permission_classes = (IsAdminUserOrRadOnly,)

    def get(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(
            skill, data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)
        self.check_object_permissions(request, skill)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
