from django.urls import path
from .views import TodoListView, TodoCreateView, TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(), name='home'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('todo/new/', TodoCreateView.as_view(), name='todo_create'),

]
