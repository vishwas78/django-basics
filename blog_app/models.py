from django.db import models

from users.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    user = models.ForeignKey(User, related_name="blog")
    date_created = models.DateField(auto_now_add=True)
    image = models.ImageField(verbose_name="Image")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

