from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')#.all()
    return render(request, 'main/index.html', {'title':'qw', 'tasks':tasks})


def create_task(request):
    if request.method == 'POST':
        error = ''
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'неверные данные формы'
    form = TaskForm()
    context = {'form': form}
    return render(request, 'main/create.html', context, error)


def about(request):
    return render(request, 'main/about.html')   