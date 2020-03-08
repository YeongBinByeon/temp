from django.contrib import admin

from todo.models import Todo, MainActionStatics


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'todo')

@admin.register(MainActionStatics)
class MainActionStaticsAdmin(admin.ModelAdmin):
    list_display = ('date', 'tv_search_title','tv_unknown_search','tv_open_search','tv_play_title')
