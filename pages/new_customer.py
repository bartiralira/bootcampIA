import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno
import seaborn as sbs
import sklearn.metrics as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.express as px
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import silhouette_score
#from tqdm import tqdm
from sklearn.decomposition import PCA
import joblib

import plotly.io as pio
pio.renderers.default = "vscode"

from pandas import read_csv
import streamlit as st
from multipage import MultiPage



def app():
    #st.markdown("## Novo cliente")
    # deixa a pagina full wide
    #st.set_page_config(layout="wide")
    #app = MultiPage()

    # preparando a sepracao da pagina
    header = st.container()
    dataset = st.container()

    modelo = joblib.load("./modelo/classificador_cliente.pkl")


    # comeca os containers
    @st.cache
    def get_data(filename):
        file= pd.read_csv(filename,sep="\t",decimal='.', engine='python')
        file = file.reindex(sorted(file.columns), axis=1)
        file.drop(file.columns[0],axis=1,inplace=True)
        return file

    with header:
        st.title("Adicionando novo cliente:")   
    
    with st.form(key='my_form'):
        ativoCirculante = st.number_input("Ativo Circulante", format="%.2f")
        capitalSocial = st.number_input('Capital Social', format="%.2f")
        custos = st.number_input('Custos', format="%.2f")
        dashboardCorrelacao=st.slider('Dashboard Correlação',-10.0,10.0,0.0)
        definicaoRisco=st.slider('Definição de risco',0, 4,0)
        empresa_MeEppMei=st.radio("Empresa ME/MEI/EPP",("Sim","Não"))
        endividamento = st.number_input('Endividamento', format="%.2f")
        estoque = st.number_input('Estoque', format="%.2f")
        faturamentoBruto = st.number_input('Faturamento Bruto', format="%.2f")
        limiteEmpresaAnaliseCredito = st.number_input('Analise de Crédito', format="%.2f")
        maiorAtraso=st.slider('Mario atraso(dias)',0, 1000)
        margemBruta = st.number_input('Margem bruta', format="%.2f")
        margemBrutaAcumulada = st.number_input('Margem bruta acumulada', format="%.2f")
        passivoCirculante = st.number_input('Passivo circulante', format="%.2f")
        percentualProtestos=st.slider('Percentual de protestos (%)',0, 100)
        prazoMedioRecebimentoVendas=st.slider('Prazo médio de recebimento de vendas',0, 1000)
        restricoes=st.radio('Restrições',("Sim","Não"))
        scorePontualidade=st.slider('Score de pontualidade',0.0, 1.0)
        titulosEmAberto = st.number_input('Títulos em aberto', format="%.2f")
        totalPatrimonioLiquido = st.number_input('Patrimonio líquido', format="%.2f")
        valorAprovado = st.number_input('Valor aprovado', format="%.2f")
        valorSolicitado = st.number_input('Valor solicitado', format="%.2f")
        submit_button = st.form_submit_button(label='Submit')
