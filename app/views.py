from django.shortcuts import render
from .models import Student, User


# Create your views here.
def index(request):
    obj1 = Student.objects.all()
    obj2 = User.objects.all()
    context = {
        "obj1": obj1,
        "obj2": obj2,
    }
    return render(request, "index.html", context)
