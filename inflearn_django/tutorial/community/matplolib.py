import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# models.py 에서 생성한 각 class를 불러온다
from django.shortcuts import render

def matplotlib_graph(request):
    FOLDER_PATH = "/home/yeongbin/code_folder/KIC/"
    dataFrame =  pd.read_excel(FOLDER_PATH + "extracted_mainAction.xlsx")
    print(dataFrame.values)
    print(dataFrame.values.ndim)
    print(dataFrame.values.shape)
    #print(dataFrame.iloc[1])
    return render(request, 'test.html', {'dataFrame':dataFrame.values})

    # post_df = post_df.merge(line_df, left_on='line_id', right_on='id', how = 'inner').drop(['id_x','id_y'],axis=1)
    # post_df = post_df.merge(problem_df, left_on='problem_id', right_on='id', how = 'inner')
    # df = post_df.merge(component_df, left_on='component_id', right_on='id', how = 'inner')
    # # 각 Dataframe 합치기

    # df_line_component = pd.DataFrame(df.groupby(['name_x']).count())
    # # 데이터 가공

    # plt.bar(df_line_component.index,df_line_component['name'])
    # # plot

    # plt.savefig('C:/Users/chongs/Desktop/production_meeting/django_project/image/graph/foo.png')
    # # image 