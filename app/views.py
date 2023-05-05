from django.shortcuts import render
from .models import MyModel

# Create your views here.
def index(request):
    obj = MyModel.objects.all()
    context = {
        "obj":obj,
    }

    return render(request,"index.html", context)
