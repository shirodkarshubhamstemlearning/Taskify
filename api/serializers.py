from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    # created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        
        model = Task
        fields = ['title', 'desc', 'assignee', 'status', 'due_date', 'created_by']
