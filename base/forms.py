from django import forms
from .models import UploadedDocument

class DocumentUploadForm(forms.ModelForm):
    participant_username = forms.CharField(max_length=150, required=False)

    class Meta:
        model = UploadedDocument
        fields = ['file']
