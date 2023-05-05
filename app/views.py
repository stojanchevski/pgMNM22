from django.shortcuts import render, redirect
from .models import MyModel, Post, PdfFile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PdfFileForm


# Create your views here.
# def index(request):
#     obj = MyModel.objects.all()
#     context = {
#         "obj":obj,
#     }
def index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
        "featured_post": posts[0],
    }

    return render(request, "index.html", context)


def upload_pdf(request):
    if request.method == 'POST':
        form = PdfFileForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.save(commit=False)
            pdf_file.save()

            return redirect('index')
    else:
        form = PdfFileForm()

        pdf_files = PdfFile.objects.all()

        return render(request, 'upload_pdf.html', {'form': form, 'pdf_files': pdf_files})
