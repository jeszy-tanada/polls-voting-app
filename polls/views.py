from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from .forms import QuestionForm
from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''
        return Question.objects.order_by('-pub_date')[:5]
        '''
        #return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message':"You didn't select a choice",
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    #return HttpResponse('You are voting on question %s.' % question_id)

def add(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if request.POST['choice_text']:
            new_choice = question.choice_set.create(
                question = question,
                choice_text = request.POST['choice_text']
            )
            new_choice.save()
            return redirect('polls:detail', pk=question.pk)
        else:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message2': "You didn't add a choice",
            })

class QuestionCreate(generic.CreateView):
    model = Question
    template_name = 'polls/question.html'
    form_class = QuestionForm
    success_url = reverse_lazy('polls:index')

    #def get_success_url(self):
        #return reverse('index', args=(self.object.id,))

    def form_valid(self, form):
        form.save()
        return super(QuestionCreate, self).form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("form is invalid.. this is just an HttpResponse object")
