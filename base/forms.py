from django import forms
from .models import UploadedDocument


from ckeditor.widgets import CKEditorWidget

class MyForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget())

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['file']