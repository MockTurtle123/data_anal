import streamlit as st
import pandas as pd
import plotly.express as px
from backend import df_preparation


df = pd.read_csv('data2.csv')
df = df_preparation(df)

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
    st.write(f'Всего проголосовало: {len(sorted_df.index)}')

    st.subheader('1. Оцените, насколько вашему ребенку нравятся занятия в Happy Panda:')

    rating_figure = px.pie(sorted_df['lesson_rating'], names='lesson_rating',)
    st.plotly_chart(rating_figure)

    average_rating = sorted_df['lesson_rating'].mean(axis=0).squeeze()
    rating_trunc = '%.2f' % average_rating
    st.write(f'Средний рейтинг: {rating_trunc}')

    lesson_ratings = []
    for index, row in sorted_df.iterrows():
        if row['lesson_rating'] not in lesson_ratings and row['lesson_rating'] < 10:
            lesson_ratings.append(row['lesson_rating'])

    st.write('Посмотреть, кто поставил рейтинг меньше 10:')
    lesson_rating_select = st.selectbox('выберите оценку:', options=sorted(lesson_ratings), index=None)
    if lesson_rating_select is not None:
        st.dataframe(sorted_df.loc[sorted_df['lesson_rating'] == lesson_rating_select][['Name', 'referer']],
                     width=500)

    st.subheader('2. Оцените работу координатора:')

    rating_figure = px.pie(sorted_df['admin_rating'], names='admin_rating', )
    st.plotly_chart(rating_figure)

    average_rating = sorted_df['admin_rating'].mean(axis=0).squeeze()
    rating_trunc = '%.2f' % average_rating
    st.write(f'Средний рейтинг: {rating_trunc}')

    admin_ratings = []
    for index, row in sorted_df.iterrows():
        if row['admin_rating'] not in admin_ratings and row['admin_rating'] < 10:
            admin_ratings.append(row['admin_rating'])

    st.write('Посмотреть, кто поставил рейтинг меньше 10:')
    admin_rating_select = st.selectbox('выберите оценку:', options=sorted(admin_ratings), index=None, key='admin_rating_select')
    if admin_rating_select is not None:
        st.dataframe(sorted_df.loc[sorted_df['admin_rating'] == admin_rating_select][['Name', 'referer']],
                     width=500)

    st.subheader('3. Оцените чистоту в офисе:')

    rating_figure = px.pie(sorted_df['cleanliness_rating'], names='cleanliness_rating', )
    st.plotly_chart(rating_figure)

    average_rating = sorted_df['cleanliness_rating'].mean(axis=0).squeeze()
    rating_trunc = '%.2f' % average_rating
    st.write(f'Средний рейтинг: {rating_trunc}')

    cleanliness_ratings = []
    for index, row in sorted_df.iterrows():
        if row['cleanliness_rating'] not in cleanliness_ratings and row['cleanliness_rating'] < 10:
            cleanliness_ratings.append(row['cleanliness_rating'])

    st.write('Посмотреть, кто поставил рейтинг меньше 10:')
    cleanliness_rating_select = st.selectbox('выберите оценку:', options=sorted(cleanliness_ratings), index=None)
    if cleanliness_rating_select is not None:
        st.dataframe(sorted_df.loc[sorted_df['cleanliness_rating'] == cleanliness_rating_select][['Name', 'referer']],
                     width=500)

    st.subheader('4. Что можно улучшить:')
    st.write('Кликните 2 раза, если комментарий не умещается, '
             'либо нажмите значок "fullscreen" в правом верхнем углу таблицы')
    filtered_df = sorted_df[sorted_df['feedback'].notnull()]
    st.dataframe(filtered_df[['Name', 'feedback']],
                 width=1000)



    # st.subheader('2. Что бы вы хотели улучшить в Happy Panda:')
    #
    # improve_dict = {}
    # improve_string = ''
    #
    # for index, row in sorted_df.iterrows():
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
    #     match improve_box:
    #         case 'Работу координатора':
    #             st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("Работу")][['Name', 'referer']],
    #                          width=500)
    #         case 'Обратную связь':
    #             st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("связь")][['Name', 'referer']],
    #                          width=500)
    #         case 'Количество мероприятий':
    #             st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("мероприятий")][['Name', 'referer']],
    #                          width=500)
    #         case 'Чистоту':
    #             st.dataframe(sorted_df.loc[sorted_df['improve'].str.contains("Чистоту")][['Name', 'referer']],
    #                          width=500)
    #
    # st.subheader('3. Как вы оцениваете работу координатора в вашем центре:')
    # admin_figure = px.histogram(sorted_df['admin_rating'])
    # st.plotly_chart(admin_figure)
    #
    # admin_ratings = ['Нейтральные', 'Равнодушные']
    #
    # st.write('Посмотреть, кто проголосовал:')
    # admin_box = st.selectbox('Выберите оценку', options=admin_ratings, index=None)
    #
    # if admin_box is not None:
    #     st.dataframe(sorted_df.loc[sorted_df['admin_rating'] == admin_box][['Name', 'referer']],
    #                  width=500)
    #
    # st.subheader('Посмотреть комментарии:')
    # st.write('Кликните 2 раза, если комментарий не умещается')
    # filtered_df = sorted_df[sorted_df['Textarea'].notnull()]
    # st.dataframe(filtered_df[['Name', 'Textarea']],
    #              width=1000)