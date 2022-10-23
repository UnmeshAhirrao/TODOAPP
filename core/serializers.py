from dataclasses import fields
from rest_framework import serializers

from core.models import ToDoItem


class ToDoItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoItem
        fields = ('id', 'created_date', 'due_date', 'description',
                  'status', 'completion_date')
