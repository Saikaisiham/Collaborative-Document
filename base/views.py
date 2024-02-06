from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedDocument
from .forms import DocumentUploadForm

# Create your views here.


def test(request):
    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None  
            document = form.save(commit=False)
            document.user = user
            document.save()
            return redirect('/') 
    else:
        form = DocumentUploadForm()

    return render(request, 'base/test.html', {'form': form})
