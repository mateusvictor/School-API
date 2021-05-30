import requests
import json 

def print_json(mydict):
	temp = json.loads(mydict)
	print(json.dumps(temp, indent=4))
"""
	{
		"id": 2,
		"person": {
			"first_name": "Jorge",
			"last_name": "Santos",
			"date_of_birth": "2001-01-23",
			"email": "jorgess@hotmail.com",
			"address": {
				"person": 5,
				"country": "Argentina",
				"state": "El Sol",
				"city": "Buenos Aires",
				"street": "Rua del Ar y Sol, 123",
				"postal_code": "912-1231-312",
				"complement": "Apto 21"
			}
		},
		"salary": "9212.12",
		"entry_year": 2009
	}
"""
def send_post():
	# data = {
	# 	"person": {
	# 		"first_name": "Maria",
	# 		"last_name": "Dores",
	# 		"date_of_birth": "2000-11-29",
	# 		"email": "maria@hotmail.com",
	# 		"address": {
	# 			"country": "Argentina",
	# 			"state": "Garrafa",
	# 			"city": "Buenos Aires",
	# 			"street": "Rua del Garrafon, 123",
	# 			"postal_code": "912-1231-312",
	# 			"complement": "Apto Feliz"
	# 		}
	# 	}
	# }
	data = {

		'professor': 4
	}
	r = requests.put('http://localhost:8000/api/professors/4/', json=data)
	print_json(r.text)
	print(r.status_code)


def send_put():
	data = send_get()
	data['salary'] = "9123.12"
	data['person']['email'] = "cuzcuz@gmail.com"
	data['person']['address']['state'] = 'São Paulo' 
	data['person']['address']['complement'] = 'Casa Verde' 
	
	r = requests.put('http://localhost:8000/api/professors/4/', json=data)
	print_json(r.text)
	print(r.status_code)


def send_get():
	r = requests.get('http://localhost:8000/api/professors/4/')
	a = r.text
	new_dict = json.loads(a)
	print_json(a)
	return new_dict
print('vaimlk')
send_put()	