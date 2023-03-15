from django.contrib import admin

# Register your models here.
from .models import Student
from .models import User
from .models import Note
from .models import Image

admin.site.register(Student)
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Image)
