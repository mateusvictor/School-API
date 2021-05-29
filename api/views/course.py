from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from api.models import *


class CourseList(APIView):
	def get(self, request):
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True)
		return Response(serializer.data)
