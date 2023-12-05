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

    st.subheader('2. Как вы оцениваете отношение преподавателя к вам?')
    teacher_figure = px.histogram(sorted_df['teacher_rating'])
    st.plotly_chart(teacher_figure)

    st.subheader('3. Как вы оцениваете уровень занятий в Happy Panda?')
    opinion_figure = px.histogram(sorted_df['client_opinion'])
    st.plotly_chart(opinion_figure)