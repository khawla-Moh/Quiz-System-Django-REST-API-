# Quiz-System-Django-REST-API-
Django REST API for a quiz system


A Django REST API for a quiz system featuring roles for Teachers and Students. Teachers can create and manage quizzes with multiple-choice questions, while Students can view and take quizzes assigned to them. The API supports JWT authentication and includes automatic grading functionality.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Postman Collection](#postman-collection)
- [Testing](#testing)
- 
## Features

- Teacher role for creating and managing quizzes.
- Student role for taking quizzes and viewing scores.
- Support for multiple-choice questions.
- Time limits for quizzes and automatic grading.
- JWT authentication for secure API access.
- Detailed API documentation via Postman collection.

## Technologies Used

- Django
- Django REST Framework
-SQLite for development
- djangorestframework-simplejwt for JWT authentication
- Postman for API testing

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/quiz-system-api.git
   cd quiz-system-api

    Create a virtual environment:
    bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
bash

pip install -r requirements.txt

Set up the database:

    Modify settings.py to configure your database settings.
    Run migrations:

bash

python manage.py migrate

Create a superuser (optional):
bash

    python manage.py createsuperuser

Usage

    Run the server:
    bash

    python manage.py runserver

    Access the API at http://localhost:8000/api/.

    Authenticate: Use the /api/token/ endpoint to obtain JWT tokens for authenticated requests.

API Endpoints
Method	Endpoint	Description
POST	/api/quizzes/	Create a new quiz (Teacher only).
GET	/api/quizzes/	List all quizzes (Authenticated users).
POST	/api/submissions/	Submit answers for a quiz (Student only).
GET	/api/submissions/{id}/	Retrieve submission details (Student).
Postman Collection

The project includes a Postman collection for testing the API. You can find it in the postman_tests directory. Import it into Postman to run tests against the API.
Testing

    Use Postman to run the provided tests.
    Ensure that your API is running before executing the tests.
