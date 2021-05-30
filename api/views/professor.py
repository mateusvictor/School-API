from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import *
from api.models import *


class ProfessorList(APIView):
	def get(self, request):
		professors = Professor.objects.all()
		serializer = ProfessorSerializer(professors, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ProfessorSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
			
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessorDetail(APIView):
	def get_object(self, pk):
		try:
			return Professor.objects.get(pk=pk)
		except Professor.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		professor = self.get_object(pk)
		serializer = ProfessorSerializer(professor)
		return Response(serializer.data)

	def put(self, request, pk):
		professor = self.get_object(pk)
		serializer = ProfessorSerializer(professor, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		professor = self.get_object(pk)		
		professor.delete()
		return Response("[]", status=status.HTTP_200_OK)
