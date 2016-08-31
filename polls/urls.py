from django.conf.urls import url
from . import views
from .models import Question, Choice

'''
The url() function is passed four arguments,
two required: regex and view, and
two optional: kwargs, and name.

index.html:
<li><a href="/polls/{{ question_d }}/">{{ question.question_text }}</a></li>

app_name = 'polls'
urlpatterns = [
    # /polls/
    url(r'^$', views.index, name='index'),
    # /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
'''
app_name = 'polls'
urlpatterns = [
    # /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/5/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/add/$', views.add, name='add'),
    #p /polls/add_question
    url(r'^question/$', views.QuestionCreate.as_view(), name='question'),
    #model=Question, success_url="index"
]
