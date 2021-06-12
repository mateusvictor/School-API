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
		},
		...
	]

## Create a new student

### Request
`post.json content`

	{
		"person": {
		    "first_name": "Jorge Vieira",
		    "last_name": "Silva Amoedo",
		    "date_of_birth": "2000-07-05",
		    "email": "jorgin@gmail.com",
		    "address": {
		        "country": "Brazil",
		        "state": "Sao Paulo",
		        "city": "Sao Paulo",
		        "street": "Rua do Paulo, 21",
		        "postal_code": "03123-901"
		    }
		},
		"salary": 1312.01
	} 


`POST /api/professors/`
	
	http POST localhost:8000/api/professors/ < post.json

### Response

	HTTP/1.1 201 Created
	Allow: GET, POST, HEAD, OPTIONS
	Content-Length: 365
	Content-Type: application/json
	Date: Sat, 12 Jun 2021 20:18:32 GMT	

	{
	    "id": 6,
	    "person": {
	        "first_name": "Jorge Vieira",
	        "last_name": "Silva Amoedo",
	        "date_of_birth": "2000-07-05",
	       	"email": "jorgin@gmail.com",
	        "address": {
	            "person": 10,
	            "country": "Brazil",
	            "state": "Sao Paulo",
	            "city": "Sao Paulo",
	            "street": "Rua do Paulo, 21",
	            "postal_code": "03123-901",
	            "complement": null
	        }
	    },
	    "salary": "1312.01",
	    "entry_year": 2021,
	    "courses_taught_count": 0,
	    "courses_taught": []
	}

## Get the list of students

### Request
`GET /api/students/`

	http localhost:8000/api/students

### Response

	HTTP/1.1 200 OK
	Allow: GET, POST, HEAD, OPTIONS
	Content-Length: 1188
	Content-Type: application/json
	Date: Sat, 12 Jun 2021 20:10:00 GMT

	[
	    {
	        "id": 1,
	        "person": {
	            "first_name": "Jorge Vieira",
	            "last_name": "Silva Amoedo",
	            "date_of_birth": "2000-07-05",
	            "email": "jorge@gmail.com",
	            "address": {
	                "person": 1,
	                "country": "Brazil",
	                "state": "Sao Paulo",
	                "city": "Sao Paulo",
	                "street": "Rua do Paulo, 21",
	                "postal_code": "03123-901",
	                "complement": null
	            }
	        },
	        "courses_enrolled_count": 1,
	        "courses_enrolled": [
	            {
	                "course": 1,
	                "student": 1,
	                "enrolled_at": "05-06-2021 13:03:55"
	            }
	        ]
	    },
	    ...
	]
