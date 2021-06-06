from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from api.models import *

def already_enrolled(student, course):
	return Enroll.objects.all().filter(student=student, course=course).exists()

class CourseList(APIView):
	def get(self, request):
		courses = Course.objects.all()
		serializer = CourseSerializer(courses, many=True, context={'request': request})
		return Response(serializer.data)

	def post(self, request):
		serializer = CourseSerializer(data=request.data, context={'request': request})

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
	def get_object(self, pk):
		try:
			return Course.objects.get(pk=pk)
		except Course.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		course = self.get_object(pk)
		serializer = CourseSerializer(course, context={'request': request})
		return Response(serializer.data)

	def put(self, request, pk):
		course = self.get_object(pk)
		serializer = CourseSerializer(course, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		course = self.get_object(pk)		
		course.delete()
		return Response("[]", status=status.HTTP_200_OK)


class EnrollView(APIView):
	def get(self, request):
		enrolls = Enroll.objects.all()
		serializer = EnrollSerializer(enrolls, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = EnrollSerializer(data=request.data)

		if serializer.is_valid():
			student, course = serializer.validated_data.values()
			print(student, course)
			if already_enrolled(student, course):
				error = {
					'error': f'Student {student} already enrolled {course}'
				}
				return Response(error, status=status.HTTP_400_BAD_REQUEST)
			else:
				serializer.save()
				data = {
					'data': f'Student {student} successfully enrolled {course}'
				}
				return Response(data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
