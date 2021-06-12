from decimal import Decimal
from django.urls import reverse
from django.forms.models import model_to_dict
import json
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import *


class ProfessorTests(APITestCase):
	def test_create_professor(self):
		"""
		Ensure we can create a new student object
		"""
		url = reverse('professor-list')
		data = { 
			'person': {
				'first_name': 'Mateus',
				'last_name': 'Victor',
				'date_of_birth': '2000-11-21',
				'email': 'victors_@yahoo.com',
				'address': {
					'country': 'Brazil',
					'state': 'Sao Paulo',
					'city': 'Sao Paulo',
					'street': 'Avenida Brasil, 2111',
					'postal_code': '21232-009',
				}
			},
			'salary': 9213.12,
			'entry_year': 2000
		}

		response = self.client.post(url, data, format='json')
		response_dict = dict(response.data)

		professor_object = Professor.objects.get(pk=int(response_dict['id']))
		person_object = professor_object.person
		address_object = person_object.address

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(data['person']['first_name'], person_object.first_name)
		self.assertEqual(data['person']['address']['street'], address_object.street)
		self.assertEqual(Decimal(str(data['salary'])), professor_object.salary)





class StudentTests(APITestCase):
	def test_create_student(self):
		"""
		Ensure we can create a new student object
		"""
		url = reverse('student-list')
		data = { 
			'person': {
				'first_name': 'Caio',
				'last_name': 'Castro',
				'date_of_birth': '1982-06-19',
				'email': 'castroo@outlook.com',
				'address': {
					'country': 'Brazil',
					'state': 'Sao Paulo',
					'city': 'Sao Paulo',
					'street': 'Avenida Brasil, 21',
					'postal_code': '01132-901',
					'complement': 'Apartamento 10'
				}
			}
		}
		response = self.client.post(url, data, format='json')
		response_dict = dict(response.data)
		student_object = Student.objects.get(pk=int(response_dict['id']))
		person_object = student_object.person
		address_object = person_object.address

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response_dict['person']['first_name'], person_object.first_name)
		self.assertEqual(response_dict['person']['address']['street'], address_object.street)
