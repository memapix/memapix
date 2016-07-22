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


def load_data_txt_to_tag_model():
    """Read data file and create Tag model objects."""

    filepath = os.path.abspath('memapixapp/static/memapixapp/data/tag_test.txt')

    with open(filepath) as f:
        for line in f:
            tag_text_from_file = line.strip()
            new_tag = Tag(tag_text=tag_text_from_file)
            new_tag.save()

    return "All tags from data file created, added to database and saved."


