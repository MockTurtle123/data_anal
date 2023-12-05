import streamlit as st
import pandas as pd
import plotly.express as px
from backend import convert_df, office_replace

df = pd.read_csv('data.csv')

df = office_replace(df)

st.title('Общий анализ (по всем центрам)')
st.subheader('1. Оцените Happy Panda от 1 до 10:')

rating_figure = px.histogram(df['rating'])
st.plotly_chart(rating_figure)

ratings = []
for index, row in df.iterrows():
    if row['rating'] not in ratings and row['rating'] < 10:
        ratings.append(row['rating'])

st.write('Посмотреть, кто поставил рейтинг меньше 10:')
rating_select = st.selectbox('выберите оценку:', options=sorted(ratings))

if rating_select is not None:
    st.dataframe(df.loc[df['rating'] == rating_select][['Name', 'referer']],
                 width=500)

st.subheader('2. Что бы вы хотели улучшить в Happy Panda:')

improve_dict = {}
improve_string = ''
for index, row in df.iterrows():
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
improve_box = st.selectbox('Выберите критерий', options=improve_dict.keys())
if improve_box is not None:
    match improve_box:
        case 'Работу координатора':
            st.dataframe(df.loc[df['improve'].str.contains("Работу")][['Name', 'referer']],
                         width=500)
        case 'Обратную связь':
            st.dataframe(df.loc[df['improve'].str.contains("связь")][['Name', 'referer']],
                         width=500)
        case 'Количество мероприятий':
            st.dataframe(df.loc[df['improve'].str.contains("мероприятий")][['Name', 'referer']],
                         width=500)
        case 'Чистоту':
            st.dataframe(df.loc[df['improve'].str.contains("Чистоту")][['Name', 'referer']],
                         width=500)

st.subheader('3. Хотели бы вы узнать больше про зимний лагерь?')

camp_figure = px.pie(df['winter_camp'], names='winter_camp')
st.plotly_chart(camp_figure)
st.write('Список проголосовавших "да":')

csv = convert_df(df)

with open("winter_camp_list.xlsx", "rb") as file:
    btn = st.download_button(
            label="скачать список",
            data=file,
            file_name="winter_camp_list.xlsx"
          )