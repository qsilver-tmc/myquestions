from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Question

question_example = {
					'title': 'Как пропатчить kde2 под freebsd?',
					'likes': 0,
					'id': 1,
					'tags': {'kde2', 'freebsd'},
					'answers': 1,
					'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'}

answer_example = {
				'likes': 0,
				'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'}


def index(request):
	questions = Question.objects.sort_date()
	objects_page, paginator = paginate(questions, request)
	questions = paginator.get_page(objects_page)
	context = {'questions': questions}
	return render(request, "index.html", context)

def ask(request):
	return render(request, "new.html", {})

def login(request):
	return render(request, "login.html", {})

def signup(request):
	return render(request, "signup.html", {})

def settings(request):
	return render(request, "settings.html", {})

def question(request, question_id):
	question = Question.objects.get(id=question_id)
	answers = question.answer_set.all
	context = {'question': question, 'answers': answers}
	return render(request, "question.html", context)

def tag(request, search_tag):
	questions = Question.objects.by_tag(search_tag)
	objects_page, paginator = paginate(questions, request)
	questions = paginator.get_page(objects_page)
	context = {'search_tag': search_tag, 'questions': questions}
	return render(request, "by_tag.html", context)

def hot(request):
	questions = Question.objects.sort_hot()
	objects_page, paginator = paginate(questions, request)
	questions = paginator.get_page(objects_page)
	context = {'questions': questions}
	return render(request, "hot.html", context)

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 3)
    objects_page = request.GET.get('page')
    if not objects_page or not objects_page.isdigit() or (int(objects_page) < 1) or (int(objects_page) > paginator.num_pages):
    		objects_page = 1
    return objects_page, paginator