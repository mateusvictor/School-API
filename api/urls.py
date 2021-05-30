from django.urls import path
from api.views import student as student_view, professor as professor_view, course as course_view


urlpatterns = [
	# Student urls
	path('students/', student_view.StudentList.as_view(), name='student-list'),
	path('students/<int:pk>/', student_view.StudentDetail.as_view(), name='student-detail'),

	# Professor urls
	path('professors/', professor_view.ProfessorList.as_view(), name='professor-list'),
	path('professors/<int:pk>/', professor_view.ProfessorDetail.as_view(), name='professor-detail'),

	# Course urls
	path('courses/', course_view.CourseList.as_view(), name='course-list'),
	path('courses/<int:pk>/', course_view.CourseDetail.as_view(), name='course-detail'),
]
