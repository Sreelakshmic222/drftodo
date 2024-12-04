from django.shortcuts import render
from rest_framework.response import Response

from .models import Task
from .serializar import TaskSerializer
from rest_framework.decorators import api_view
# Create your views here.

#following function based
@api_view(['Get'])
def tasks_overview(request):
    api_urls={
        'List':'/tasks-list',
        'Detail':'/tasks-detail/<int id>',
        'Create':'/tasks-create/',
        'Update':'/tasks-update/<int id>',
        'Delete':'/tasks-delete/<int id>'
    }
    return Response(api_urls)

@api_view(['Get'])
def showall(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

# View for rendering the task list page
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

@api_view(['Post'])
def createtask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# View for task details
def viewtask(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'task_detail.html', {'task': task})

@api_view(['Post'])
def updatetsk(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['Get'])
def deletetask(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Product deleted sucessfully")

def home(request):
    return render(request, 'home.html')