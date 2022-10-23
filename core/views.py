from rest_framework import generics

from core.models import ToDoItem
from core.serializers import ToDoItemSerializer

class TodoItemListCreateView(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer


class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer