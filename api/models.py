from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from api.utils import current_year


class Person(models.Model):
	"""Model representing a Person """
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	date_of_birth = models.DateField()
	email = models.EmailField(unique=True)


class Address(models.Model):
	"""Model representing an Addreess"""
	person = models.OneToOneField(Person, related_name='address', on_delete=models.CASCADE)
	country = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	street = models.CharField(max_length=200)
	postal_code = models.CharField(max_length=100)
	complement = models.CharField(max_length=100, null=True, blank=True)


class Professor(models.Model):
	"""Model represnting a Professor"""
	person = models.OneToOneField(Person, related_name='person', on_delete=models.CASCADE)
	salary = models.DecimalField(max_digits=10, decimal_places=2)
	entry_year = models.PositiveIntegerField(
		default=current_year(),
		validators=[
			MinValueValidator(1980),
			MaxValueValidator(current_year())])

	def courses_taught_count(self):
		return self.courses_taught.all().count()

	def __str__(self):
		return f'{self.person.first_name} {self.person.last_name}'


class Student(models.Model):
	"""Model representing a Student"""
	person = models.OneToOneField(Person, on_delete=models.CASCADE)

	def courses_enrolled_count(self):
		return self.courses_enrolled.all().count() # Reverse relation from Student to Enroll

	def __str__(self):
		return f'{self.person.first_name} {self.person.last_name}'


class Course(models.Model):
	"""Model representing a Course"""
	name = 	models.CharField(max_length=100)
	description = models.CharField(max_length=300, null=True, blank=True)
	professor = models.ForeignKey(Professor, related_name='courses_taught', on_delete=models.SET_NULL, null=True)

	def students_count(self):
		"""Returns the count of the students that enrolled the course"""
		return self.course_instances.all().count() # Reverse relation from Course to Enroll

	def __str__(self):
		return f'{self.name}'


class Enroll(models.Model):
	"""Model representing a Course Instance (created when a user register in a new course)"""
	enrolled_at = models.DateTimeField(auto_now=True)
	course = models.ForeignKey(Course, related_name='course_instances', on_delete=models.CASCADE)
	student = models.ForeignKey(Student, related_name='courses_enrolled', on_delete=models.CASCADE)
