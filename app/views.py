from django.shortcuts import render, redirect
from .models import MyModel, Post, PdfFile, PostDE
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PdfFileForm
from .index_post_generator import all_data
from django.http import FileResponse
from django.shortcuts import get_object_or_404


# Create your views here.
# def index(request):
#     obj = MyModel.objects.all()
#     context = {
#         "obj":obj,
#     }
def index(request):
    posts = Post.objects.all()
    files = PdfFile.objects.all()

    context = {
        "posts": all_data,
        "featured_post": all_data[0],
        "files": files,
    }

    return render(request, "index.html", context)


def download_file(request, file_id):
    pdf_file = get_object_or_404(PdfFile, id=file_id)
    file_path = pdf_file.file.path
    file_name = pdf_file.file.name.split('/')[-1]  # Extracts the filename from the path
    file = open(file_path, 'rb')
    response = FileResponse(file)
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
    return response



