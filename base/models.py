from django.db import models

class UploadedDocument(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploaded_documents/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
