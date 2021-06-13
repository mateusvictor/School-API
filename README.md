# School-API
A REST API made using Django Rest Framework and PostgreSQL where students can enroll/unenroll courses, check the courses enrolled and more. (Check the REST API section)

The project also contains a documentation made with swagger: (check <a href="http://localhost:8000">localhost:8000</a> after installing for the more details)

<img src="https://github.com/mateusvictor/School-API/blob/main/swagger-ui.png">

# How to use it?

- First Clone this repo

```bash
git clone https://github.com/mateusvictor/School-API.git
```

- Change into the project directory

```bash
cd path_to_project/school_api/
```

- Create a Virtualenv and the project directory

```bash
python -m venv venv
```

- Activate the virtualenv

```bash
venv\Scripts\activate.bat
```

- Install the project dependencies

```bash
pip install -r requirements.txt
```

# Database configurations

- First open your ```psql terminal``` and type:

```sql
CREATE DATABASE school_api;
```

- Make sure you change the ```DATABASES``` dictionary on <a href="https://github.com/mateusvictor/School-API/blob/main/school_api/settings.py">settings.py</a> to this:

```python
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'school_api',
            'USER': 'YOUR_USERNAME',
            'PASSWORD': 'YOUR_PASSWORD',
            'HOST': 'localhost',
            'PORT': '5432',
        },
        ...
}
```

* PS .: Note that there is a sqlite database right below the ```default``` database, so if you want to just use the stantard Django sqlite you can change the ```DATABASES``` dictionary like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

- Finally, make the migrations on the database choosed:

```bash
python manage.py migrate
```

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

## Create a new professor

### Request
`post.json content`

```json
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
```

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

## Create a new student

### Request
`post.json content`

```json
{
    "person": {
        "first_name": "Jorge Vieira",
        "last_name": "Silva Amoedo",
        "date_of_birth": "2000-07-05",
        "email": "joao@gmail.com",
        "address": {
            "country": "Brazil",
            "state": "Sao Paulo",
            "city": "Sao Paulo",
            "street": "Rua do Paulo, 21",
            "postal_code": "03123-901"
        }
    }
} 
```


`POST /api/students/`
    
    http POST localhost:8000/api/students/ < post.json


### Response

    HTTP/1.1 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Length: 331
    Content-Type: application/json
    Date: Sat, 12 Jun 2021 21:29:58 GMT

    {
        "id": 6,
        "person": {
            "first_name": "Jorge Vieira",
            "last_name": "Silva Amoedo",
            "date_of_birth": "2000-07-05",
            "email": "joao@gmail.com",
            "address": {
                "person": 12,
                "country": "Brazil",
                "state": "Sao Paulo",
                "city": "Sao Paulo",
                "street": "Rua do Paulo, 21",
                "postal_code": "03123-901",
                "complement": null
            }
        },
        "courses_enrolled_count": 0,
        "courses_enrolled": []
    }

## Get list of courses

### Request
`GET /api/courses/`
    
    http localhost:8000/api/courses/

### Response
    
    HTTP/1.1 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Length: 433
    Content-Type: application/json
    Date: Sat, 12 Jun 2021 21:35:28 GMT

    [
        {
            "id": 1,
            "name": "Algorithms",
            "description": "A nice overview of Algorithms",
            "professor": 1,
            "students_count": 3,
            "course_instances": [
                {
                    "course": 1,
                    "student": 2,
                    "enrolled_at": "05-06-2021 13:01:30"
                }
            ]
        },
        {
            "id": 2,
            "name": "Biology",
            "description": "High School Biology",
            "professor": null,
            "students_count": 0,
            "course_instances": []
        }
    ]

## Create a new course

### Request
`post.json content`

```json
{
    "name": "Biology",
    "description": "High School Biology",
    "professor": 1
}
```

`POST /api/courses/`
    
    http POST localhost:8000/api/courses/ < post.json

### Response

    HTTP/1.1 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Length: 116
    Content-Type: application/json
    Date: Sat, 12 Jun 2021 21:49:06 GMT

    {
        "id": 4,
        "name": "Biology",
        "description": "High School Biology",
        "professor": 1,
        "students_count": 0,
        "course_instances": []
    }


## Enroll a student in an existing course

### Request
`post.json content`

```json
{
    "course": 1,
    "student": 5
}
```

`POST /api/courses/enroll/`

    http localhost:8000/api/courses/enroll/ < post.json

### Response
    
    HTTP/1.1 201 Created
    Allow: GET, POST, HEAD, OPTIONS
    Content-Length: 77
    Content-Type: application/json
    Date: Sat, 12 Jun 2021 22:00:19 GMT

    {
        "data": "Student Jorge Vieira Silva Amoedo successfully enrolled Algorithms"
    }

