from django.views.generic import TemplateView
from django.shortcuts import render

class TodoTV(TemplateView):
    template_name = 'todo/todo_index.html'

class chartjs(TemplateView):
    template_name = 'todo/chartjs.html'

    def get(self, request, data, *args, **kwargs):
        print(data)
        #return render(request, self.template_name, {'aaa':'3, 5, 7, 9, 11, 13'})
        return render(request, self.template_name, {'aaa':data})