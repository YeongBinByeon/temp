

from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoTV.as_view(), name='index'),
    path('chartjs/<data>', views.chartjs.as_view(), name='chartjs'),
]
