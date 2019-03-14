# Website urls
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # namespace is for situations when more than one app contains views with the same name. Specificity
    url(r'^music/', include('music.urls', namespace='music')), # when music page is requested, head over to the music app's url file to handle the request
]
# whenever we're in developer mode, use the media directory we specified in settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)