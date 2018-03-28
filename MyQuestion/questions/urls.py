from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask, name='ask'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('tag/<search_tag>/', views.tag, name='tag'),
    path('hot/', views.hot, name='hot')
]

