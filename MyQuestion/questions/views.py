from django.shortcuts import render

def index(request):
	questions = []
	for i in range(0,5):
  		questions.append({
		'title': 'Как пропатчить kde2 под freebsd?',
		'likes': 0,
		'tags': {'kde2', 'freebsd'},
		'answers': 1,
		'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})
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
	question = {
		'title': 'Как пропатчить kde2 под freebsd?',
		'likes': 0,
		'tags': {'kde2', 'freebsd'},
		'answers': 1,
		'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'}
	
	answers = []
	for i in range(0,2):
  		answers.append({
		'likes': 0,
		'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})

	context = {'question': question, 'answers': answers}
	return render(request, "question.html", context)

def tag(request, search_tag):
	questions = []
	for i in range(0,5):
  		questions.append({
		'title': 'Как пропатчить kde2 под freebsd?',
		'likes': 0,
		'tags': {'kde2', 'freebsd'},
		'answers': 1,
		'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})
	context = {'search_tag': search_tag, 'questions': questions};
	return render(request, "by_tag.html", context)

def hot(request):
	questions = []
	for i in range(0,5):
  		questions.append({
		'title': 'Как пропатчить kde2 под freebsd?',
		'likes': 0,
		'tags': {'kde2', 'freebsd'},
		'answers': 1,
		'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'})
	context = {'questions': questions}
	return render(request, "hot.html", context)