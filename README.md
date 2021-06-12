# School-API
A REST API made using Django Rest Framework and PostgreSQL where students can enroll/unenroll courses, check the courses enrolled and more. (Check routes)

# REST API

## Get the list of professors

### Request
`GET /api/professors/`

	http localhost:8000/api/professors

### Response

	HTTP/1.1 200 OK
	Allow: GET, POST, HEAD, OPTIONS
	Content-Length: 376
	Content-Type: application/json
	Date: Sat, 12 Jun 2021 19:58:00 GMT

	[
		{
			"id": 1,
			"person": {
				"first_name": "Rodolfo",
				"last_name": "Castro",
				"date_of_birth": "1980-01-10",
				"email": "rodolfo@gmail.com",
				"address": {
					"person": 4,
					"country": "Brazil",
					"state": "Rio de Janeiro",
					"city": "Rio de Januario",
					"street": "Rua do Fevereiro, 2311",
					"postal_code": "11013-100",
					"complement": null
				}
			},
			"salary": "10000.91",
			"entry_year": 2021,
			"courses_taught_count": 1,
			"courses_taught": [
				1
			]
		}
	]