from django.shortcuts import render, redirect
from tasks.adapters.repository import TaskRepository
from tasks.application.services import TaskService

# View -> service -> repository
repo = TaskRepository()
service = TaskService(repo)
#this adapter talks to users, handles input/output.
def task_list(request):
    error = None

    if request.method == 'POST':
        title = request.POST.get('title', '')
        due_date = request.POST.get('due_date', '')
        priority = request.POST.get('priority', 'normal')

        try:
            service.create_task(title, due_date, priority)
            return redirect('task_list')
        except Exception as e:
            error = str(e)
    #goes to the service to get all the tasks 
    tasks = service.get_all_tasks()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'error': error})


def delete_task(request, task_id):
    service.delete_task(task_id)
    return redirect('task_list')


def edit_task(request, task_id):
    task = service.get_task(task_id)
    error = None

    if request.method == 'POST':
        title = request.POST.get('title', '')
        due_date = request.POST.get('due_date', '')
        priority = request.POST.get('priority', 'normal')

        try:
            service.update_task(task_id, title, due_date, priority)
            return redirect('task_list')
        except Exception as e:
            error = str(e)

    return render(request, 'tasks/edit_task.html', {'task': task, 'error': error})
