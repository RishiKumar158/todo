from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("update/<int:id>", views.UpdateTask, name="update"),
	path("delete/<int:id>", views.DeleteTask, name = "delete")
]
