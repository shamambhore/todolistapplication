import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        task_t = request.POST['tasktitle']
        task_d = request.POST['taskdesc']
        tasks = Task()
        tasks.task_title =task_t
        tasks.task_desc = task_d
        tasks.save()
        context = {'success': True}   
    return render(request, 'home.html', context)

def viewtask(request):
    task_data = Task.objects.all()
    context = {'tasks': task_data}
    return render(request, 'viewtask.html', context)
