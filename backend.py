import pandas as pd
import streamlit as st

df = pd.read_csv('data.csv')

@st.cache_data
def office_replace(df):
    df = df.replace(['https://happypanda-center.ru/newsamara'], 'Новая Самара')
    df = df.replace(['https://happypanda-center.ru/yjka'], 'Южный Город')
    df = df.replace(['https://happypanda-center.ru/dmitrovsk'], 'Дмитр. Шоссе')
    df = df.replace(['https://happypanda-center.ru/ovrag'], 'Овраг')
    df = df.replace(['https://happypanda-center.ru/radamira'], 'Радамира')
    df = df.replace(['https://happypanda-center.ru/lublin'], 'Люблино')
    df = df.replace(['https://happypanda-center.ru/volgaropros'], 'Волгарь')
    df = df.replace(['https://happypanda-center.ru/kievskagagarina'], 'Киевская / Гагарина')
    df = df.replace(['https://happypanda-center.ru/metallurg'], 'Металлург')
    df = df.replace(['https://happypanda-center.ru/postnikovovrag'], 'Овраг')
    return df


@st.cache_data
def convert_df(df):
    df = df.loc[df['winter_camp'] == 'Да'][['Name', 'teacher', 'referer']]
    return df.to_csv()