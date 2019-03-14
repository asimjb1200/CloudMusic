from django.conf.urls import url
from . import views # importing the created functions

# creating a namespace, this creates specificity if we have several urls under the same names
app_name = 'music'

urlpatterns = [
    # /music/ - This url pattern will be under the name "IndexView"
    url(r'^$', views.IndexView.as_view(), name='index'), 
    
    # /music/<pk>/ - the number in the url will be saved as <pk> and we'll pass it to the DetailsView class in views
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'), # detail will be the name of this url pattern

    # /music/album/add/  this url is for when we want to create a new album
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2/  this url is for when we want to update an album with a primary key of <pk>
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]