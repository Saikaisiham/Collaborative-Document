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

@login_required
def test(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None  
            document = form.save(commit=False)
            document.user = user
            document.save()
            
            # docx_content = document.document.read()
            # doc = Document(io.BytesIO(docx_content))
            # html_content = render_to_string('document_detail.html', {'doc': doc})
            # return HttpResponse(html_content)
            return redirect('/', file_id=document.id)
    else:
        form = DocumentUploadForm()

    return render(request, 'base/test.html', {'form': form})


# def document_detail(request, file_id):
#     uploaded_file = get_object_or_404(UploadedDocument, pk=file_id)
#     if uploaded_file.file.name.endswith('.odt'):
#         file_content = convert_odt_to_html(uploaded_file.file.path)
#     else:
#         with open(uploaded_file.file.path, 'r') as file:
#             file_content = file.read()
#     return render(request, 'base/document_detail.html', {'file_content': file_content})


def document_detail(request, id):
    uploaded_file = get_object_or_404(UploadedDocument, id=id)
    

    with uploaded_file.file.open('rb') as file_content:
        file_binary = file_content.read()
    
    encoding_info = chardet.detect(file_binary)
    encoding = encoding_info['encoding']
    
    file_content_decoded = file_binary.decode('latin-1')
    return render(request, 'base/document_detail.html', {'file_content_decoded': file_content_decoded})
