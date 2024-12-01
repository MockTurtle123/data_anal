import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')

@st.cache_data
def df_preparation(df):
    df = pd.read_csv('data2.csv')

    df = df.drop(df.columns[[12, 14, 15, 16, 17, 18]], axis=1)

    df = df.replace(['https://happypanda-center.ru/novayasamara'], 'Новая Самара')
    df = df.replace(['https://happypanda-center.ru/dmitrovskoe'], 'Дмитр. Шоссе')
    df = df.replace(['https://happypanda-center.ru/Revolyucionnaya'], 'Овраг')
    df = df.replace(['https://happypanda-center.ru/radamira'], 'Радамира')
    df = df.replace(['https://happypanda-center.ru/lyublinoos'], 'Люблино')
    df = df.replace(['https://happypanda-center.ru/volgaros'], 'Волгарь')
    df = df.replace(['https://happypanda-center.ru/gagarina'], 'Гагарина')
    df = df.replace(['https://happypanda-center.ru/metallurgos'], 'Металлург')
    df = df.replace(['https://happypanda-center.ru/vesennyaya'], 'Весенняя')
    df = df.replace(['https://happypanda-center.ru/ddonskogo'], 'ЮГ2')
    df = df.replace(['https://happypanda-center.ru/nikolaevsky'], 'Ник42')
    df = df.replace(['https://happypanda-center.ru/kievskaya'], 'Киевская')

    df.columns.values[1] = "course"
    df.columns.values[2] = "teacher"
    df.columns.values[3] = "lesson_rating"
    df.columns.values[4] = "teacher_rating"
    df.columns.values[5] = "admin_rating"
    df.columns.values[6] = "cleanliness_rating"
    df.columns.values[7] = "friend_reference"
    df.columns.values[12] = "feedback"

    # df['teacher_rating'] = df['teacher_rating'].astype(int)

    return df


# @st.cache_data
# def convert_df(df):
#     df = df.loc[df['winter_camp'] == 'Да'][['Name', 'teacher', 'referer']]
#     return df.to_csv()