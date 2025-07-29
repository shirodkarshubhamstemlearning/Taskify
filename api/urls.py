from django.urls import path
from .views import ShowTasks, CreateTasks, SingleTask, UpdateTask, DeleteTask

urlpatterns = [
    path('api/tasks/show_tasks/', ShowTasks.as_view(), name='show-tasks'),
    path('api/tasks/create_tasks/', CreateTasks.as_view(), name='create-tasks'),
    path('api/tasks/sole_task/<int:pk>', SingleTask.as_view(), name='sole-tasks'),
    path('api/tasks/update_task/<int:pk>', UpdateTask.as_view(), name='update-tasks'),
    path('api/tasks/delete_task/<int:pk>', DeleteTask.as_view(), name='delete-tasks'),
]
