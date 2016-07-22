from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(models.Model):
    """class User"""

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    date_joined = models.DateTimeField('date joined')

    def __str__(self):
        """object representation"""

        return "{}, {}".format(str(self.id), self.username)


@python_2_unicode_compatible
class Album(models.Model):
    """class Album"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')

    def __str__(self):
        """object representation"""

        return "{}, {}".format(str(self.id), self.title)


@python_2_unicode_compatible
class Tag(models.Model):
    """class Tag"""

    tag_text = models.CharField(max_length=200)

    def __str__(self):
        """object representation"""

        return "{}, {}".format(str(self.id), self.tag_text)



@python_2_unicode_compatible
class Photo(models.Model):
    """class Photo"""

    albums = models.ManyToManyField(Album)
    tags = models.ManyToManyField(Tag)
    processed = models.BooleanField()
    url = models.URLField(max_length=200)
    date_added = models.DateTimeField('date added')
    caption_text = models.CharField(max_length=200)

    def __str__(self):
        """object representation"""

        return "{}, {}".format(str(self.id), self.caption_text)






