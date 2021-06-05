from rest_framework import serializers
from api.models import *


def update_instance(instance, validated_data):
	"""Update all the instance's fields specified in the validated_data"""
	for key, value in validated_data.items():
		setattr(instance, key, value)
	return instance.save()


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
		fields = ['id', 'person']

	def create(self, validated_data):
		person_data = validated_data.pop('person')
		person = PersonSerializer(data=person_data)

		if person.is_valid():
			person_inst = person.save()

		student = Student.objects.create(person=person_inst)
		return student 

	def update(self, instance, validated_data):
		"""
		Update method: an expansable method so that any new Student/Person/Address field will be updated
		Reused in `ProfessorSerializer` class
		"""
		person_data = validated_data.pop('person')
		address_data = person_data.pop('address')

		update_instance(instance, validated_data)
		update_instance(instance.person, person_data)
		update_instance(instance.person.address, address_data)

		return instance


class ProfessorSerializer(StudentSerializer):
	"""PersonSerializer: inherits the `.update()` method and the `person` variable from StudentSerializer"""

	class Meta:
		model = Professor
		fields = ['id', 'person', 'salary', 'entry_year']

	def create(self, validated_data):	
		person_data = validated_data.pop('person')
		person = PersonSerializer(data=person_data)

		if person.is_valid():
			person_inst = person.save()

		professor = Professor.objects.create(person=person_inst, **validated_data)
		return professor


class CourseSerializer(serializers.ModelSerializer):
	professor_link = serializers.HyperlinkedRelatedField(read_only=True, view_name='professor-detail')
	
	class Meta:
		model = Course
		fields = ['id', 'name', 'description', 'professor', 'professor_link']


class EnrollSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enroll
		fields = ['student', 'course']
	