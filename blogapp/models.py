from django.db import models


class PostType(models.Model):  # article categories
    name = models.CharField("Name", max_length=50, )

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ManyToManyField('PostType')
    title = models.CharField("Title", max_length=150, )
    post = models.TextField("Post", max_length=150, )

    def __str__(self):
        return self.title

    def __str__(self):
        return self.post
