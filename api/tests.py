from api.models import *
from datetime import date

# p1 = Person(
# 	first_name='Jorge Vieira',
# 	last_name='Silva Amoedo',
# 	date_of_birth=date(2000, 7, 5),
# 	email='jorge@gmail.com').save()

# p2 = Person(
# 	first_name='Isabela',
# 	last_name='Caieiras',
# 	date_of_birth=date(1990, 1, 5),
# 	email='isa_caieiras@gmail.com').save()

# p3 = Person(
# 	first_name='Rodolfo',
# 	last_name='Castro',
# 	date_of_birth=date(1980, 1, 10),
# 	email='rodolfo@gmail.com').save()


# p1 = Person.objects.get(pk=1)
# p2 = Person.objects.get(pk=2)
# p3 = Person.objects.get(pk=3)

# add1 = Address(
# 	person=p1,
# 	country='Brazil',
# 	state='Sao Paulo',
# 	city='Sao Paulo', 
# 	street='Rua do Paulo, 21',
# 	postal_code='03123-901')
# add1.save()

# add2 = Address(
# 	person=p2,
# 	country='Noruega',
# 	state='Shistei',
# 	city='Poted Breiks', 
# 	street='North Street, 21',
# 	postal_code='21123-911')
# add2.save()

# add3 = Address(
# 	person=p3,
# 	country='Brazil',
# 	state='Rio de Janeiro',
# 	city='Rio de Januario', 
# 	street='Rua do Fevereiro, 2311',
# 	postal_code='11013-100')
# add3.save()

# std1 = Student(person=p1)
# std1.save()

# std2 = Student(person=p2)
# std2.save()

# prof1 = Professor(person=p3, salary=10000.91)
# prof1.save()
# co1 = Course(
# 	name='Algorithms',
# 	description='A nice overview of Algorithms',
# 	professor=prof1)
# co1.save()

# co2 = Course(
# 	name='Biology',
# 	description='High School Biology',
# 	professor=prof1)
# co2.save()

# enr1 = Enroll(
# 	course=co1,
# 	student=std1).save()

# enr2 = Enroll(
# 	course=co2,
# 	student=std1).save()

# enr3 = Enroll(
# 	course=co1,
# 	student=std2).save()

# std1 = Student.objects.get(pk=1)
# std2 = Student.objects.get(pk=2)
# prof1 = Professor.objects.get(pk=1)

# co1 = Course.objects.get(pk=1)
# co2 = Course.objects.get(pk=2)

from api.models import *
from api.serializers import *

import json


def print_json(mydict):
	temp = json.loads(json.dumps(mydict))
	print(json.dumps(temp, indent=4))


data = {
	'person': {
		'first_name': 'Maria', 
		'last_name': 'Dores',
		'date_of_birth': '2000-11-29',
		'email': 'maria@hotmail.com',
		'address': {
			'country': 'Argentina',
			'state': 'Garrafa',
			'city': 'Buenos Aires',
			'street': 'Rua del Garrafon, 123',
			'postal_code': '912-1231-312',
		}
	},
	'entry_yar': 2009,
	'salary': 9212.12
}

sery = StudentSerializer(data=data)
sery.is_valid()
