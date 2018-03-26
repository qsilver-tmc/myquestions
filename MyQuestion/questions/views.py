from django.shortcuts import render

def index(request):
	return render(request, "index.html", {})

def new(request):
	return render(request, "new.html", {})

def login(request):
	return render(request, "login.html", {})

def signup(request):
	return render(request, "signup.html", {})

def settings(request):
	return render(request, "settings.html", {})

def question(request):
	return render(request, "question.html", {})

def tag(request):
	return render(request, "by_tag.html", {})