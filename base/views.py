from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import UploadedDocument
from .forms import DocumentUploadForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from docx import Document
import io
from .utils import convert_odt_to_html
from django.shortcuts import get_object_or_404
import zipfile
from io import BytesIO
import chardet
import mimetypes
import docx
import os

@login_required
def test(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None  
            document = form.save(commit=False)
            document.user = user
            document.save()
            return redirect('/', file_id=document.id)
    else:
        form = DocumentUploadForm()

    return render(request, 'base/test.html', {'form': form})





def document_detail(request, id):
    uploaded_file = get_object_or_404(UploadedDocument, id=id)
    
    file_path = uploaded_file.file.path
    
    if os.access(file_path, os.R_OK):
        print("File is readable.")
    else:
        print("File is not readable.")
    mime_type, _ = mimetypes.guess_type(file_path)

    try:
        doc = docx.Document(file_path)
        content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        content = "Error occurred while reading the Word document: {}".format(str(e))

    if mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':

        try:
            doc = docx.Document(file_path)
            content = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        except Exception as e:
            content = "Error occurred while reading the Word document: {}".format(str(e))
    else:

        with open(file_path, 'rb') as file:
            file_content = file.read()

        if mime_type and mime_type.startswith('text'):
            content = file_content.decode('utf-8')
        else: 
            content = "Can't decode the file. Mime type: {}".format(mime_type)

    return render(request, 'base/document_detail.html', {'content': content})