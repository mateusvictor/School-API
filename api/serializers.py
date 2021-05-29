from rest_framework import serializers
from api.models import *


class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = ['person', 'country','state', 'city', 'street', 'postal_code', 'complement']
		read_only_fields = ('person', )


class PersonSerializer(serializers.ModelSerializer):
	address = AddressSerializer()

	class Meta:
		model = Person
		fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'address']

	def create(self, validated_data):
		address_data = validated_data.pop('address')
		person = Person.objects.create(**validated_data)
		address = Address.objects.create(person=person, **address_data)

		return person


class StudentSerializer(serializers.ModelSerializer):
	person = PersonSerializer()

	class Meta:
		model = Student
		fields = ['person']

	def create(self, validated_data):
		person_data = validated_data.pop('person')
		person = PersonSerializer(data=person_data)

		if person.is_valid():
			person_inst = person.save()

		student = Student.objects.create(person=person_inst)
		return student 


class ProfessorSerializer(serializers.ModelSerializer):
	person = PersonSerializer()

	class Meta:
		model = Professor
		fields = ['person', 'salary', 'entry_year']

	def create(self, validated_data):	
		person_data = validated_data.pop('person')
		person = PersonSerializer(data=person_data)

		if person.is_valid():
			person_inst = person.save()

		professor = Professor.objects.create(person=person_inst, **validated_data)
		return professor


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ['name', 'description', 'professor']
