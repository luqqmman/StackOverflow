from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='forum-index'),
    path('login', views.login, name='forum-login'),
    path('question', views.question, name='forum-question'),
    path('my_question', views.my_question, name='forum-my-question'),
    path('my_answer', views.my_answer, name='forum-my-answer'),
    path('my_comment', views.my_comment, name='forum-my-comment'),
]
