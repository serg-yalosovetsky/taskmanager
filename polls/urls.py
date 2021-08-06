from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('polls', views.about, name='polls'),
    # path('create_task', views.create_task, name='create'),
]
