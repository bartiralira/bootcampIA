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


header = st.container()
dataset = st.container()

modelo = joblib.load("./modelo/classificador_cliente.pkl")

@st.cache
def get_data(filename):
    file= pd.read_csv(filename,sep="\t",decimal='.', engine='python')
    file.drop(file.columns[1],axis=1,inplace=True)
    return file

st.sidebar.title("BootcampIA - Turma 17IA")
st.sidebar.markdown("Equipe: Bartira, Vitor, Tiago e Ricardo")

with header:
    st.title("Criando clusters:")   
    
with dataset:
    st.subheader("Clusters gerados")
    df = get_data('datasetclusterizado.csv')

    cluster=pd.to_numeric(df.cluster.unique())
    #df["Permanência Origem (h)"] = df["Permanência Origem (h)"].astype(int)
    #pd.to_numeric(df["Permanência Origem (h)"])
    #df["Permanência no Destino (h)"] = pd.to_numeric(df["Permanência no Destino (h)"])
    #selecao = sel_col.selectbox("Select",origem[["Local TD"]], index=0)
    cluster_min=int(cluster.min())
    cluster_max=int(cluster.max())
    sel_col= st.columns(1)

    selecao = st.slider("Select",min_value=cluster_min, max_value=cluster_max)

with dataset:

    X_minmax = MinMaxScaler().fit_transform(df.values)
    df_norm = pd.DataFrame(X_minmax)
    df_norm.columns = df.columns
    df_norm['cluster'] = modelo.labels_ #bestKmeans.labels_
    #df_norm.head()  
    df_res = df_norm.groupby('cluster',as_index=False).mean()
    
    #plt.figure(1, figsize=(32, 10))
    #fig, axes = plt.subplots(1, figsize=(32,10))
    fig = px.bar(df_res, x="cluster", y=df_res.columns, title="Wide-Form Input")
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=False,height=400,)
    st.write(fig)



with dataset:
    labels = modelo.labels_
    qtdClusters = len(set(labels))

    plt.figure(figsize=(10,10))
    fig, axes = plt.subplots(nrows=qtdClusters, ncols=1, figsize=(20,15))

    for c in set(labels):        
        medias =  df_norm[ df_norm.cluster== c].mean()
        medias.drop(['cluster'], inplace = True)
        medias.plot(ax = axes[c], kind='bar', fontsize=8, title = 'Cluster: ' + str(c), rot=15 )
    
    fig.tight_layout()
    st.write(fig)