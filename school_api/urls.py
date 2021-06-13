from django.contrib import admin
from django.conf.urls.static import static
from school_api import settings
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
	path('openapi/', get_schema_view(
		title="School API made using Django Rest Framework",
		description="Here you can read, create, edit and delete professors, students, courses and more.",
		version="1.0.0"
	), name='openapi-schema'),

	path('', TemplateView.as_view(
		template_name='swagger-ui.html',
		extra_context={'schema_url':'openapi-schema'}
	), name='swagger-ui'),	
]