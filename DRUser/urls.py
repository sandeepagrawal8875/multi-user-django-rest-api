from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls 

schema_view = get_schema_view(title='buyer or seller API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('core.urls', namespace='api')),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Buyer or Seller API')),

]
