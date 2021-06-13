from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.datastructures import MultiValueDictKeyError
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
			"""
		 	`_, _ = serializer.validated_data['...'], serializer.validated_data['...']` is a better aproach
			than `serializer.validated_data.values()` because it avoid errors if the order of the fields on 
			EnrollSerializer is changed
			"""
			student, course = serializer.validated_data['student'], serializer.validated_data['course']


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


class UnenrollView(APIView):
	def post(self, request):
		try:
			student_id, course_id = int(request.data['student']), int(request.data['course'])
			enroll_object = Enroll.objects.get(student__id=student_id, course__id=course_id)
		
		except Enroll.DoesNotExist:
			raise Http404

		except:
			return Response({'detail': 'Student/Course id was not provided'}, 
				status=status.HTTP_400_BAD_REQUEST)
		
		enroll_object.delete()
		student = Student.objects.get(pk=student_id)
		course = Course.objects.get(pk=course_id)

		return Response({'detail': f'Student {student} successfully unenrolled {course} course'}, status=status.HTTP_200_OK)
