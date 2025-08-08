from django.shortcuts import get_object_or_404
from .serializers import TaskSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class ShowTasks(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)

            if not serializer.data:
                return Response(
                    {'message': 'No tasks found. Please create your first task.'},
                    status=status.HTTP_200_OK
                )

            return Response(
                {'Tasks': serializer.data},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    'error': 'An error occurred while retrieving tasks.',
                    'details': str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class CreateTasks(APIView):

    permission_classes = [IsAuthenticated]
    
    # @swagger_auto_schema(request_body=TaskSerializer)
    @swagger_auto_schema(
        request_body=TaskSerializer,
        security=[{'Bearer': []}],  # ← Tells Swagger this endpoint requires auth
    )
    def post(self, request):
        # created_by = request.user
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(assignee=request.user, created_by=request.user)
                return Response(
                    {
                        'Task': serializer.data,
                        'message': 'Task created successfully.'
                    },
                    status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response(
                    {
                        'error': 'An error occurred while saving the task.',
                        'details': str(e)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {
                    'error': 'Invalid input.',
                    'details': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
class SingleTask(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = get_object_or_404(Task, pk=pk)
            serializer = TaskSerializer(task)
            return Response(
                {
                    'Task': serializer.data,
                    'message': 'Task found successfully.'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    'error': 'Task not found. Please create a task or provide a valid Task ID.',
                    'details': str(e)
                },
                status=status.HTTP_404_NOT_FOUND
            )

class UpdateTask(APIView):

    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(
        request_body=TaskSerializer,
        security=[{'Bearer': []}],  # ← Tells Swagger this endpoint requires auth
    )
    def put(self, request, pk):
        
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data)
        
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(
                    {'task': serializer.data, 'message': 'Task is updated successfully'},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'error': 'An internal server error occurred while updating the task'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {'errors': serializer.errors, 'message': 'Invalid input data'},
                status=status.HTTP_400_BAD_REQUEST
            )

class DeleteTask(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            task.delete()
            return Response({'message': 'Task deleted successfully'})
        except Exception as e:
                return Response(
                    {'error': 'An internal server error occurred while updating the task'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
