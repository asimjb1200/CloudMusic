from django.db import models
from django.urls import reverse
# ONly do migrations if you add or delete columns/attributes to the database
# python manage.py makemigrations music
# then - python manage.py migrate

# Create table for database, each variable represents a column
# these tables will automatically make a unique primary key named 'id' for each 'album' made
class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    album_logo = models.FileField() # Allow the user to upload an image file
    # whenever a new album is made, return the details page of the new album that was made
    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})
    

    # this is a special method that gives a string representation of the object
    def __str__(self):
        # we now specify what that string will be
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    # we need to associate the songs with an album, so make a foreign key
    # models.cascade...once we delete an album that contains the song, delete the song as well
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    #lets make a string representation of a song
    def __str__(self):
        return self.song_title