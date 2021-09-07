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


# deixa a pagina full wide
st.set_page_config(layout="wide")


# preparando a sepracao da pagina
header = st.container()
dataset = st.container()
app = MultiPage()
modelo = joblib.load("./modelo/classificador_cliente.pkl")


# comeca os containers
@st.cache
def get_data(filename):
    file= pd.read_csv(filename,sep="\t",decimal='.', engine='python')
    file = file.reindex(sorted(file.columns), axis=1)
    file.drop(file.columns[0],axis=1,inplace=True)
    return file


# sidebar
st.sidebar.title("BootcampIA - Turma 17IA")
st.sidebar.markdown("Equipe: Bartira, Vitor, Tiago e Ricardo")

#faz as escolhas das paginas
radioButton = st.sidebar.radio("Go to",['Home', 'Novo Cliente'])
if (radioButton == "Home"):
    app.add_page("Home", home.app)

with header:
    st.title("Adicionando novo cliente:")   