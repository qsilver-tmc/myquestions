from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

from .models import Question

def index(request):
	questions = Question.objects.sort_date()
	questions = paginate(questions, request)

	context = {'questions': questions}
	return render(request, "index.html", context)

def hot(request):
	questions = Question.objects.sort_hot()
	questions = paginate(questions, request)

	context = {'questions': questions}
	return render(request, "hot.html", context)

def tag(request, search_tag):
	questions = Question.objects.by_tag(search_tag)
	questions = paginate(questions, request)
	
	context = {'search_tag': search_tag, 'questions': questions}
	return render(request, "by_tag.html", context)

def question(request, question_id):
	try:
		question = Question.objects.get(id=question_id)
	except Question.DoesNotExist:
		raise Http404("Poll does not exist")

	answers = question.answer_set.all
	
	context = {'question': question, 'answers': answers}
	return render(request, "question.html", context)



def ask(request):
	return render(request, "new.html", {})

def login(request):
	return render(request, "login.html", {})

def signup(request):
	return render(request, "signup.html", {})

def settings(request):
	return render(request, "settings.html", {})


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    objects_page = request.GET.get('page')
    if not objects_page or not objects_page.isdigit() or (int(objects_page) < 1) or (int(objects_page) > paginator.num_pages):
    		objects_page = 1

    objects_list = paginator.get_page(objects_page)
    return objects_list