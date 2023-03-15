- [images](https://djangocentral.com/uploading-images-with-django/)
- [import MEDIA_ROOT](https://stackoverflow.com/questions/5517950/django-media-url-and-media-root)
- [display all the images in a folder by using django](https://stackoverflow.com/questions/47809932/how-to-display-all-the-images-in-a-folder-by-using-django#:~:text=you%20can%20use%20file%20methods,your%20template%20using%20template%20tags.)

Secondary References:
--------------------
- [Django 4.1 models](https://docs.djangoproject.com/en/4.1/topics/db/models/)
- [forms.py](https://stackoverflow.com/questions/45618541/where-should-the-forms-py-file-be-located)
- [Django 4.1 forms](https://docs.djangoproject.com/en/4.1/topics/forms/)
- Code:

Views.py

```
def gallery_view(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + "(path to image folder in media)")
    context = {"images": img_list}
    return render (request, '(path to django template)', context)
```

Template

```
{% for image in images %}
<img  src="{{MEDIA_URL}}path to image folder{{image}}">
{% endfor %}
```

[How to display all the images in a folder by using django](https://stackoverflow.com/questions/47809932/how-to-display-all-the-images-in-a-folder-by-using-django)

- Code:

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # ... the rest of your URLconf goes here ...
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

[Django MEDIA_URL and MEDIA_ROOT](https://stackoverflow.com/questions/5517950/django-media-url-and-media-root)

- Code:

```
# settings.py

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'static',
]
```

[Can't load static image in django when using a loop](https://stackoverflow.com/questions/61442571/cant-load-static-image-in-django-when-using-a-loop)

- Text and Code:

```
try

MEDIA_URL = '/media/'
and in template

<img src="/media/blabla.jpg" />
Also put these lines of code inside your urls.py and set DEBUG to True

if settings.DEBUG:
  # static files (images, css, javascript, etc.)
  urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': settings.MEDIA_ROOT}))

```

[Site on localhost not displaying image](https://stackoverflow.com/questions/12741807/site-on-localhost-not-displaying-image)