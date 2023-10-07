from django.urls import path  
from task_api.views import TasksView, TaskDetailView
  
urlpatterns = [
    path("", TasksView.as_view()),   
    path("<str:pk>", TaskDetailView.as_view())
]
