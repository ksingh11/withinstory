from django.db import models
from django.contrib.auth.models import User, UserManager
from tastypie.models import create_api_key


class UserProfile(User):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = UserManager()
    
    def __unicode__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=50)
    introduction = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(UserProfile)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return '%s - %s' % (self.title, self.author)
    
    class Meta:
        verbose_name_plural = 'Stories'

models.signals.post_save.connect(create_api_key, sender=UserProfile)
