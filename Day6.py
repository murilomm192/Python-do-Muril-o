import streamlit as st

import pandas as pd
import polars as pl

from datetime import datetime

import streamlit as st

st.set_page_config(page_title='Análise de Dados - Atacadão', page_icon=':bar_chart:', layout='wide', initial_sidebar_state='auto')

base = pl.read_csv('atacadao_10-7.csv', infer_schema_length=1000, try_parse_dates=True)

base = base.head(10).with_columns([
    pl.lit(False).alias('Conhece o Produto?'),
    pl.lit('Barato').alias('Precepção do Preço')
])

def save_data():
    print('salvo')

st.header('Análise de Dados - Atacadão')

dados = st.data_editor(base.to_pandas(), hide_index=True, key='dados',
               column_config={
                   'imagem' : st.column_config.ImageColumn('Foto', width='medium'),
                   'data' : st.column_config.DateColumn('Data', width='medium', format='DD/MM/YYYY'),
                   'Precepção do Preço': st.column_config.SelectboxColumn(options=['Barato', 'Normal', 'Caro'], required=True),
               })

col1, col2, col3 = st.columns(3)

with col1:
    st.text_input('Nome do Validador', value='', key='nome_validador')

with col2:        
    st.date_input('Data de Validaçao', value=datetime.now(), min_value=datetime.now(), format='DD/MM/YYYY', key='data_validacao')

with col3:
    btn_ok = st.button('Salvar Dados', on_click=save_data, key='botao')

st.write(st.session_state['dados'])

dados.to_csv('salvo.csv', index=False)





