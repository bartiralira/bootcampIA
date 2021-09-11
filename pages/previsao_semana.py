import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno
import seaborn as sbs
import sklearn.metrics as sm
import matplotlib.pyplot as plt
#from tqdm import tqdm
from keras.models import load_model
import joblib

import plotly.io as pio
pio.renderers.default = "vscode"

from pandas import read_csv
import streamlit as st
from multipage import MultiPage

# comeca os containers
def app():
    #st.markdown("## Novo cliente")
    # deixa a pagina full wide
    #st.set_page_config(layout="wide")
    #app = MultiPage()

    # preparando a sepracao da pagina
    header = st.container()
    col1, col2 = st.columns(2)

    model_dia = load_model("./modelo/modelodia.hdf5")
    model_semana = load_model("./modelo/modelosemanal.hdf5")


    with header:
        st.title("Previsão de volume de crédito:")
        st.text("")
        st.text("")

    with col1: 
        form1 = st.form(key='my_form1')
        qtd_dias=form1.slider('Quantidade de dias:',0, 30,0)
        valor_dia_button = form1.form_submit_button(label='Previsão diária')
        if valor_dia_button:
            previsao_dia =model_dia.predict(qtd_dias)
            #imprimindo valor sugerido na tela
            st.write(f'Previsão diária: {previsao_dia}')
    
    with col2: 
        form2 = st.form(key='my_form2')
        qtd_semanas=form2.slider('Quantidade de semana:',0, 30,0)
        valor_semana_button = form2.form_submit_button(label='Previsão semanal')
        if valor_semana_button:
            previsao_semana =model_semana.predict(qtd_semanas)
            #imprimindo valor sugerido na tela
            st.write(f'Previsão semanal: {previsao_semana}')