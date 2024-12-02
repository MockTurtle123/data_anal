import streamlit as st
import pandas as pd
import plotly.express as px
from backend import df_preparation

df = pd.read_csv('data2.csv')
df = df_preparation(df)
df = df[df['teacher'].notna()]

teacher_list = []
for index, row in df.iterrows():
    if row['teacher'] not in teacher_list:
        teacher_list.append(row['teacher'])


teacher_select = st.selectbox('',
                              options=sorted(teacher_list),
                              placeholder='Выберите преподавателя',
                              index=None)

if teacher_select is not None:
    sorted_df = df.loc[df['teacher'] == teacher_select]

    st.write(f'Всего проголосовало: {len(sorted_df.index)}')

    st.subheader('1. Оцените, насколько вашему ребенку нравятся занятия в Happy Panda:')

    rating_figure = px.pie(sorted_df['lesson_rating'], names='lesson_rating', )
    rating_figure.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(rating_figure)

    st.write('Посмотреть, кто проголосовал:')
    rating_options = []
    for index, row in sorted_df.iterrows():
        if row['lesson_rating'] not in rating_options:
            rating_options.append(row['lesson_rating'])

    motivation_box = st.selectbox('Выберите оценку', options=rating_options, index=None)
    if motivation_box is not None:
        st.dataframe(sorted_df.loc[sorted_df['lesson_rating'] == motivation_box][['Name', 'referer']],
                     width=500)

    st.subheader('2. Оцените отношение педагога к вам и вашему ребенку:')
    teacher_figure = px.pie(sorted_df['teacher_rating'], names='teacher_rating', )
    teacher_figure.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(teacher_figure)

    st.write('Посмотреть, кто проголосовал:')

    teacher_options = []
    for index, row in sorted_df.iterrows():
        if row['teacher_rating'] not in teacher_options:
            teacher_options.append(row['teacher_rating'])

    teacher_box = st.selectbox('Выберите оценку', options=teacher_options, index=None)
    if teacher_box is not None:
        st.dataframe(sorted_df.loc[sorted_df['teacher_rating'] == teacher_box][['Name', 'referer']],
                     width=500)

    st.subheader('3. Что можно улучшить:')
    st.write('Кликните 2 раза, если комментарий не умещается, '
             'либо нажмите значок "fullscreen" в правом верхнем углу таблицы')
    filtered_df = sorted_df[sorted_df['feedback'].notnull()]
    st.dataframe(filtered_df[['Name', 'feedback']],
                 width=1000)