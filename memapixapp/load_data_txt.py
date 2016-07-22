"""Loads text data into models."""

from memapixapp.models import Photo, Tag, Album, User
import os
from django.utils import timezone


def load_data_txt_to_photo_model():
    """Read data file and create Photo model objects."""

    filepath = os.path.abspath('memapixapp/static/memapixapp/data/photo_test.txt')

    with open(filepath) as f:
        for line in f:
            photo_url, photo_caption, processed_bool = line.strip().split("|")  # split the line by the delimiter "|" and unpack directly
            new_photo = Photo(url=photo_url, caption_text=photo_caption, processed=processed_bool, date_added=timezone.now())
            new_photo.save()  # must save for data to be in database

    return "All photos from data file created, added to database and saved."


def load_data_txt_to_user_model():
    """Read data file and create User model objects."""

    filepath = os.path.abspath('memapixapp/static/memapixapp/data/user_test.txt')

    with open(filepath) as f:
        for line in f:
            username, password, first_name, last_name, email, date = line.strip().split("|") # split the line by the delimeter "|" and unpack User attributes.
            new_user = User(username=username, password=password, first_name=first_name, last_name=last_name, email=email, date_joined=timezone.now())
            new_user.save()

    return "All users from data file created, added to database and saved."


def load_data_txt_to_album_model():
    """Read data file and create Album model objects."""

    filepath = os.path.abspath('memapixapp/static/memapixapp/data/album_test.txt')

    user = User.objects.get(pk=1)
    with open(filepath) as f:
        for line in f:
            title = line.strip()
            new_album = Album(user=user, title=title, date_created=timezone.now())
            new_album.save()


    return "All albums from data file created, added to database and saved."


def load_data_txt_to_tag_model():
    """Read data file and create Tag model objects."""

    filepath = os.path.abspath('memapixapp/static/memapixapp/data/tag_test.txt')

    with open(filepath) as f:
        for line in f:
            tag_text_from_file = line.strip()
            new_tag = Tag(tag_text=tag_text_from_file)
            new_tag.save()

    return "All tags from data file created, added to database and saved."



