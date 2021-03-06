import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
#from .forms import QuestionForm

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date_published')
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
