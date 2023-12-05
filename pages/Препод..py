import streamlit as st
import pandas as pd
import plotly.express as px
from backend import office_replace

df = pd.read_csv('data.csv')
df = office_replace(df)

teacher_list = {}
for index, row in df.iterrows():
    if row['teacher'] not in teacher_list:
        teacher_list[row['teacher']] = 1
    else:
        teacher_list[row['teacher']] += 1

teacher_select = st.selectbox('',
                              options=sorted(teacher_list.keys()),
                              placeholder='Выберите преподавателя',
                              index=None)

if teacher_select is not None:
    sorted_df = df.loc[df['teacher'] == teacher_select]

    st.write(f'Всего отзывов оставлено: {teacher_list[teacher_select]}')

    st.subheader('1. Нравятся ли вашему ребенку занятия в Happy Panda?')

    motivation_series = pd.Series(sorted_df['student_motivation'])
    motivation_figure = px.histogram(motivation_series,
                                     labels={'x': "отзыв клиента", "y": "количество голосов"})
    st.plotly_chart(motivation_figure)

    st.write('Посмотреть, кто проголосовал:')
    motivation_options = []
    for index, row in sorted_df.iterrows():
        if row['student_motivation'] not in motivation_options:
            motivation_options.append(row['student_motivation'])

    motivation_box = st.selectbox('Выберите оценку', options=motivation_options, index=None)
    if motivation_box is not None:
        st.dataframe(sorted_df.loc[sorted_df['student_motivation'] == motivation_box][['Name', 'referer']],
                     width=500)

    st.subheader('2. Как вы оцениваете отношение преподавателя к вам?')
    teacher_figure = px.histogram(sorted_df['teacher_rating'])
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

    st.subheader('3. Как вы оцениваете уровень занятий в Happy Panda?')
    opinion_figure = px.histogram(sorted_df['client_opinion'])
    st.plotly_chart(opinion_figure)

    st.write('Посмотреть, кто проголосовал:')

    opinion_options = []
    for index, row in sorted_df.iterrows():
        if row['client_opinion'] not in opinion_options:
            opinion_options.append(row['client_opinion'])

    opinion_box = st.selectbox('Выберите оценку', options=opinion_options, index=None)
    if opinion_box is not None:
        st.dataframe(sorted_df.loc[sorted_df['client_opinion'] == opinion_box][['Name', 'referer']],
                     width=500)

    st.subheader('Посмотреть комментарии:')
    st.write('Кликните 2 раза, если комментарий не умещается')
    filtered_df = sorted_df[sorted_df['Textarea'].notnull()]
    st.dataframe(filtered_df[['Name', 'Textarea']],
                 width=1000)