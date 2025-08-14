from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    # title = models.CharField(max_length=255, null=False, blank=False)
    title = serializers.CharField(max_length=255)
    status = serializers.CharField()

    class Meta:
        
        model = Task
        fields = ['id', 'title', 'desc', 'assignee', 'status', 'due_date', 'created_by']
    
    def validate(self, data):
        if not data['title']:
            raise serializers.ValidationError("Title is required")
        
        if not data['desc']:
            raise serializers.ValidationError("Description is required")
        
        if not data['assignee']:
            raise serializers.ValidationError("Assignee is required")
        
        if not data['status']:
            raise serializers.ValidationError("Status is required")
        
        if not data['due_date']:
            raise serializers.ValidationError("Due date is required")
        
        return data
    