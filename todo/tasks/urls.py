from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='home'),  # Home page,
      path('tasks-list/',views.task_list,name='tasks-list'),
      path('create/',views.createtask,name='task-create'),
      path('detail/<int:pk>',views.viewtask,name='task-view'),
      path('update/<int:pk>',views.updatetsk,name='task-update'),
      path('delete/<int:pk>',views.deletetask,name='task-delete')
       ]