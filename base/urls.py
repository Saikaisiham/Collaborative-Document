from django.urls import path 
from .views import test , document_detail


urlpatterns = [
    path('', test, name='test'),
    path('doc/<int:id>/', document_detail, name='doc')
]