from django.shortcuts import render
from .models import Student, User, Note, Image
from django.conf import settings
import os
from django.conf.urls.static import static


# Create your views here.
def index(request):
    obj1 = Student.objects.all()
    obj2 = User.objects.all()
    context = {
        "obj1": obj1,
        "obj2": obj2,
    }
    return render(request, "index.html", context)


def note(request):
    obj3 = Note.objects.all()
    obj4 = Image.objects.all()
    context = {
        "obj3": obj3,
        "obj4": obj4,
    }
    return render(request, "note.html", context)


from .forms import ImageForm


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, "image.html", {"form": form, "img_obj": img_obj})
    else:
        form = ImageForm()
    return render(request, "image.html", {"form": form})


def gallery_view(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "(path to image folder in media)")
    context = {"images": img_list}
    return render(request, "(path to django template)", context)
