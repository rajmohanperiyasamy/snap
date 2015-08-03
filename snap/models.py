from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext as _
from django.conf import settings
from django.contrib.auth.models import User

# from imagekit.models import ImageSpecField, ProcessedImageField
# from imagekit.processors import ResizeToFill, SmartResize


class Article(models.Model):
    title = models.CharField(max_length=200)
    article_subject=models.CharField(max_length=50,null=True,blank=True)
    summary = models.TextField(null=True,blank=True)
    created_by= models.ForeignKey(User)
    
class Comment(models.Model):
    comment = models.CharField(max_length=2500)
    commented_by= models.ForeignKey(User)
    article = models.ForeignKey(Article)
    commented_on = models.DateTimeField(auto_now_add=True)
    
