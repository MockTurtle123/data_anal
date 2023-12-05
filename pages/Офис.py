import streamlit as st
import pandas as pd
import plotly.express as px
from backend import office_replace


df = pd.read_csv('data.csv')
df = office_replace(df)

office_list = []
for index, row in df.iterrows():
    if row['referer'] not in office_list:
        office_list.append(row['referer'])

office_select = st.selectbox('',
                             options=office_list,
                             placeholder='Выберите офис',
                             index=None)

if office_select is not None:

    sorted_df = df.loc[df['referer'] == office_select]

    st.subheader('1. Оцените Happy Panda от 1 до 10:')

    rating_figure = px.histogram(sorted_df['rating'])
    st.plotly_chart(rating_figure)

    average_rating = sorted_df['rating'].mean(axis=0).squeeze()
    rating_trunc = '%.2f' % average_rating
    st.write(f'Средний рейтинг: {rating_trunc}')

    ratings = []
    for index, row in sorted_df.iterrows():
        if row['rating'] not in ratings and row['rating'] < 10:
            ratings.append(row['rating'])

    st.write('Посмотреть, кто поставил рейтинг меньше 10:')
    rating_select = st.selectbox('выберите оценку:', options=sorted(ratings), index=None)
    if rating_select is not None:
        st.dataframe(sorted_df.loc[sorted_df['rating'] == rating_select][['Name', 'referer']],
                     width=500)


    st.subheader('2. Что бы вы хотели улучшить в Happy Panda:')

    improve_dict = {}
    improve_string = ''

    for index, row in sorted_df.iterrows():
        improve_string += (row['improve'])
    improve_dict['Ничего'] = improve_string.count('Ничего')
    improve_dict['Работу координатора'] = improve_string.count('координатора')
    improve_dict['Обратную связь'] = improve_string.count('связь')
    improve_dict['Количество мероприятий'] = improve_string.count('мероприятий')
    improve_dict['Чистоту'] = improve_string.count('Чистоту')

    improve_series = pd.Series(improve_dict)
    improve_figure = px.histogram(improve_series,
                                  x=improve_dict.keys(),
                                  y=improve_dict.values(),
                                  labels={'x': "что улучшить", "y": "количество голосов"})
    st.plotly_chart(improve_figure)

    st.write('Посмотреть, кто проголосовал:')
    improve_box = st.selectbox('Выберите критерий', options=improve_dict.keys(), index=None)
    if improve_box is not None:
        match improve_box:
            case 'Работу координатора':
                st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("Работу")][['Name', 'referer']],
                             width=500)
            case 'Обратную связь':
                st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("связь")][['Name', 'referer']],
                             width=500)
            case 'Количество мероприятий':
                st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("мероприятий")][['Name', 'referer']],
                             width=500)
            case 'Чистоту':
                st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("Чистоту")][['Name', 'referer']],
                             width=500)

    st.subheader('3. Как вы оцениваете работу координатора в вашем центре:')
    admin_figure = px.histogram(sorted_df['admin_rating'])
    st.plotly_chart(admin_figure)

    admin_ratings = ['Нейтральные', 'Равнодушные']

    st.write('Посмотреть, кто проголосовал:')
    admin_box = st.selectbox('Выберите оценку', options=admin_ratings, index=None)

    if admin_box is not None:
        st.dataframe(sorted_df.loc[sorted_df['admin_rating'] == admin_box][['Name', 'referer']],
                     width=500)

    st.subheader('Посмотреть комментарии:')
    st.write('Кликните 2 раза, если комментарий не умещается')
    filtered_df = sorted_df[sorted_df['Textarea'].notnull()]
    st.dataframe(filtered_df[['Name', 'Textarea']],
                 width=1000)