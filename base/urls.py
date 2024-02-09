from django.urls import path 
from .views import base , document_detail


urlpatterns = [
    path('', base, name='base'),
    path('doc/<int:id>/', document_detail, name='doc')
]