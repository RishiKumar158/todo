from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
	tasks = Task.objects.all()
	form = TaskForm
	if request.method == "POST":
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")
	return render(request, "tasks/list.html", { "tasks": tasks, "form": form })


def UpdateTask(request, id):
	task = Task.objects.get(pk = id)
	form = TaskForm(instance=task)
	if request.method == "POST":
		form = TaskForm(request.POST, instance=task) # if you didn't give instance it will create new TASK
		if form.is_valid():
			form.save()
			return redirect("/")

	return	render(request, "tasks/update_task.html", {"form": form})

def DeleteTask(request, id):
	task = Task.objects.get(pk = id)
	if request.method == "POST":
		task.delete()
		return redirect("/")
	return render(request, "tasks/delete.html", {"task": task})