from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('todo/', views.TodoView.as_view(), name='all-todo'),
    path('todo/<str:username>', views.TodoView.as_view(), name='id-todo-usr'),
]
