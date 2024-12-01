import streamlit as st
import pandas as pd
import plotly.express as px
from backend import df_preparation

df = pd.read_csv('data2.csv')

df = df_preparation(df)

st.title('Общий анализ (по всем центрам)')

st.subheader('1. Оцените, насколько вашему ребенку нравятся занятия в Happy Panda:')
course_options = ['Раннее развитие',
                  'Английский язык',
                  'Подготовка к школе',
                  'Изобразительное искусство']

course_select = st.selectbox('Выберите направление:', index=None, options=course_options)
if course_select is not None:
    course_df = df.loc[df['course'] == course_select]
    course_figure = px.pie(course_df['lesson_rating'], names='lesson_rating')
    st.write(f'Всего проголосовало: {len(course_df.index)}')
    st.plotly_chart(course_figure)

else:
    rating_figure = px.pie(df['lesson_rating'], names='lesson_rating')
    st.plotly_chart(rating_figure)

lesson_ratings = []
for index, row in df.iterrows():
    if row['lesson_rating'] not in lesson_ratings and row['lesson_rating'] < 10:
        lesson_ratings.append(row['lesson_rating'])

st.write('Посмотреть, кто поставил рейтинг меньше 10:')
rating_select1 = st.selectbox('выберите оценку:', options=sorted(lesson_ratings), index=None)

if rating_select1 is not None:
    st.dataframe(df.loc[df['lesson_rating'] == rating_select1][['Name', 'referer']],
                 width=500)


st.subheader('2. Оцените отношение педагога к вам и вашему ребенку:')

rating_figure = px.pie(df['teacher_rating'], names='teacher_rating')
st.plotly_chart(rating_figure)

teacher_ratings = []
for index, row in df.iterrows():
    if row['teacher_rating'] not in teacher_ratings and row['teacher_rating'] < 10:
        teacher_ratings.append(row['teacher_rating'])

st.write('Посмотреть, кто поставил рейтинг меньше 10:')
rating_select2 = st.selectbox('выберите оценку:', options=sorted(teacher_ratings), index=None)

if rating_select2 is not None:
    st.dataframe(df.loc[df['teacher_rating'] == rating_select2][['Name', 'referer']],
                 width=500)


st.subheader('3. Оцените работу координатора:')

rating_figure = px.pie(df['admin_rating'], names='admin_rating')
st.plotly_chart(rating_figure)

admin_ratings = []
for index, row in df.iterrows():
    if row['admin_rating'] not in admin_ratings and row['admin_rating'] < 10:
        admin_ratings.append(row['admin_rating'])

st.write('Посмотреть, кто поставил рейтинг меньше 10:')
rating_select3 = st.selectbox('выберите оценку:', options=sorted(admin_ratings), index=None)

if rating_select3 is not None:
    st.dataframe(df.loc[df['admin_rating'] == rating_select3][['Name', 'referer']],
                 width=500)


st.subheader('4. Оцените чистоту в центре:')

rating_figure = px.pie(df['cleanliness_rating'], names='cleanliness_rating')
st.plotly_chart(rating_figure)

cleanliness_ratings = []
for index, row in df.iterrows():
    if row['cleanliness_rating'] not in cleanliness_ratings and row['cleanliness_rating'] < 10:
        cleanliness_ratings.append(row['cleanliness_rating'])

st.write('Посмотреть, кто поставил рейтинг меньше 10:')
rating_select4 = st.selectbox('выберите оценку:', options=sorted(cleanliness_ratings), index=None)

if rating_select4 is not None:
    st.dataframe(df.loc[df['cleanliness_rating'] == rating_select4][['Name', 'referer']],
                 width=500)


# st.subheader('2. Что бы вы хотели улучшить в Happy Panda:')
#
# improve_dict = {}
# improve_string = ''
# for index, row in df.iterrows():
#     improve_string += (row['improve'])
# improve_dict['Ничего'] = improve_string.count('Ничего')
# improve_dict['Работу координатора'] = improve_string.count('координатора')
# improve_dict['Обратную связь'] = improve_string.count('связь')
# improve_dict['Количество мероприятий'] = improve_string.count('мероприятий')
# improve_dict['Чистоту'] = improve_string.count('Чистоту')
#
# improve_series = pd.Series(improve_dict)
# improve_figure = px.histogram(improve_series,
#                               x=improve_dict.keys(),
#                               y=improve_dict.values(),
#                               labels={'x': "что улучшить", "y": "количество голосов"})
# st.plotly_chart(improve_figure)
#
# st.write('Посмотреть, кто проголосовал:')
# improve_box = st.selectbox('Выберите критерий', options=improve_dict.keys(), index=None)
# if improve_box is not None:
#     if improve_box == 'Работу координатора':
#         st.dataframe(df.loc[df['improve'].str.contains("Работу")][['Name', 'referer']],
#                      width=500)
#     elif improve_box == 'Обратную связь':
#         st.dataframe(df.loc[df['improve'].str.contains("связь")][['Name', 'referer']],
#                      width=500)
#     elif improve_box == 'Количество мероприятий':
#         st.dataframe(df.loc[df['improve'].str.contains("мероприятий")][['Name', 'referer']],
#                      width=500)
#     elif improve_box == 'Чистоту':
#         st.dataframe(df.loc[df['improve'].str.contains("Чистоту")][['Name', 'referer']],
#                      width=500)
#
#
# st.subheader('3. Как вы оцениваете занятия в Happy Panda?')
# course_options = ['Раннее развитие',
#                  'Английский язык',
#                  'Подготовка к школе',
#                  'Частная школа Панда Академия',
#                  'Изобразительное искусство']
#
# course_select = st.selectbox('Выберите направление:', index=None, options=course_options)
# if course_select is not None:
#     course_df = df.loc[df['course'] == course_select]
#     course_figure = px.pie(course_df['client_opinion'], names='client_opinion')
#     st.write(f'Всего проголосовало: {len(course_df.index)}')
#     st.plotly_chart(course_figure)
#
#
# st.subheader('4. Хотели бы вы узнать больше про зимний лагерь?')
#
# camp_figure = px.pie(df['winter_camp'], names='winter_camp')
# st.plotly_chart(camp_figure)
# st.write('Список проголосовавших "да":')
#
# csv = convert_df(df)
#
# with open("winter_camp_list.xlsx", "rb") as file:
#     btn = st.download_button(
#             label="скачать список",
#             data=file,
#             file_name="winter_camp_list.xlsx"
#           )