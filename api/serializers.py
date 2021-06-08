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


class EnrollSerializer(serializers.ModelSerializer):
	enrolled_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

	class Meta:
		model = Enroll
		fields = ['course', 'student', 'enrolled_at']


class StudentSerializer(serializers.ModelSerializer):
	person = PersonSerializer()
	courses_enrolled = EnrollSerializer(many=True, read_only=True)
	courses_enrolled_count = serializers.SerializerMethodField()

	class Meta:
		model = Student
		fields = ['id', 'person', 'courses_enrolled_count', 'courses_enrolled']

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

	def get_courses_enrolled_count(self, obj):
		return obj.courses_enrolled_count()

class CourseSerializer(serializers.ModelSerializer):	
	course_instances = EnrollSerializer(many=True, read_only=True)
	students_count = serializers.SerializerMethodField()

	class Meta:
		model = Course
		fields = ['id', 'name', 'description', 'professor', 'students_count', 'course_instances']

	def get_students_count(self, obj):
		return obj.students_count()


class ProfessorSerializer(StudentSerializer):
	"""PersonSerializer: inherits the `.update()` method and the `person` variable from StudentSerializer"""
	courses_taught = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	courses_taught_count = serializers.SerializerMethodField()

	class Meta:
		model = Professor
		fields = ['id', 'person', 'salary', 'entry_year', 'courses_taught_count', 'courses_taught']

	def create(self, validated_data):	
		person_data = validated_data.pop('person')
		person = PersonSerializer(data=person_data)

		if person.is_valid():
			person_inst = person.save()

		professor = Professor.objects.create(person=person_inst, **validated_data)
		return professor

	def get_courses_taught_count(self, obj):
		return obj.courses_taught_count()