from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class UploadedDocument(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    participants = models.ManyToManyField('auth.User', related_name='uploaded_documents')
    file = models.FileField(upload_to='uploaded_documents/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
