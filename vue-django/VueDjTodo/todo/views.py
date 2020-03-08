from django.views.generic import TemplateView, ListView, CreateView
from django.shortcuts import render
import pandas as pd
from .models import MainActionStatics

from io import BytesIO
from urllib.parse import quote
from django.http import HttpResponse

class TodoTV(TemplateView):
    template_name = 'todo/todo_index.html'

class chartjs(TemplateView):
    template_name = 'todo/chartjs.html'

    def get(self, request, data, *args, **kwargs):
        print(data)
        #return render(request, self.template_name, {'aaa':'3, 5, 7, 9, 11, 13'})
        return render(request, self.template_name, {'aaa':data})

# 작성하는데 참조한 블로그 링크 : https://okky.kr/article/641816
class updatedb(CreateView):
    template_name = 'todo/todo_index.html'
    Model = MainActionStatics
    df = pd.read_excel(r'C:\code_folder\temp\vue-django\VueDjTodo\todo\data_file\20200305.xlsx')
    print(df)
    print(df.index)
    print(df['date'].iloc[0])
    print(df['tv_search_title'].iloc[0] )
    #MainActionStatics(date=df['date'].iloc[0], tv_search_title=df['tv_search_title'].iloc[0], tv_unknown_search=df['tv_unknown_search'].iloc[0], tv_open_search=df['tv_open_search'].iloc[0], tv_play_title=df['tv_play_title'].iloc[0]).save()
    queryset = MainActionStatics.objects.create(date=df['date'].iloc[0], tv_search_title=df['tv_search_title'].iloc[0], tv_unknown_search=df['tv_unknown_search'].iloc[0], tv_open_search=df['tv_open_search'].iloc[0], tv_play_title=df['tv_play_title'].iloc[0])
    # def get(self, request, *args, **kwargs):
    #     self.object_list = self.get_queryset()
    #     print(self.object_list)
    #     #return super().get(request, *args, **kwargs)
   
def excel(request):
    df = pd.DataFrame([
        [100,200,300],
        [200,300,400],
    ])
    io = BytesIO()
    df.to_excel(io)
    io.seek(0)
    encoded_filename = quote('pandas.xlsx')
    response = HttpResponse(io, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    return response