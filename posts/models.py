from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    choices = {
        ('YOGA', 'YOGA'),
        ('PILATES', 'PILATES'),
        ('GŁOS', 'GŁOS'),
        ('ŻYCIE', 'ŻYCIE'),
    }

    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(default='', blank=False, null=False)
    kind = models.CharField(max_length=32, choices=choices, blank=False, null=False)
    cover = models.ImageField(upload_to='post_covers', blank=False, null=False)
    text = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()

        return super(Post, self).save(*args, **kwargs)


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=False, null=False)
