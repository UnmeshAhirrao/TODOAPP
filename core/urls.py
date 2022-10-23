from django.urls import path
from core.views import TodoItemDetailView, TodoItemListCreateView

app_name = 'core'

urlpatterns = [
    path('todo-items/', TodoItemListCreateView.as_view(), name='todo_list'),
    path('todo-items/<int:pk>/', TodoItemDetailView.as_view(), name='todo_item'),
]