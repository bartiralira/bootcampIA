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
#st.set_page_config(layout="wide")
def app():
    #st.markdown("## Clusterizando")

    # preparando a sepracao da pagina
    header = st.container()
    overview = st.container()
    cluster0 = st.container()
    cluster1 = st.container()
    cluster2 = st.container()
    cluster3 = st.container()
    cluster4 = st.container()
    #app = MultiPage()
    modelo = joblib.load("./modelo/classificador_cliente.pkl")


    # comeca os containers
    @st.cache
    def get_data(filename):
        file= pd.read_csv(filename,sep="\t",decimal='.', engine='python')
        file = file.reindex(sorted(file.columns), axis=1)
        file.drop(file.columns[0],axis=1,inplace=True)
        return file

    with header:
        st.title("Clusterizando:")   

        df = get_data('./data/datasetclusterizado.csv')

        cluster=pd.to_numeric(df.cluster.unique())
        cluster_min=int(cluster.min())
        cluster_max=int(cluster.max())
        sel_col= st.columns(1)

        

    with overview:

        X_minmax = MinMaxScaler().fit_transform(df.values)
        df_norm = pd.DataFrame(X_minmax)
        df_norm.columns = df.columns
        df_norm['cluster'] = modelo.labels_ #bestKmeans.labels_
        #df_norm.head()  
        
        # seletor
        selecao = st.multiselect("Selecione a variável",df_norm.columns)
        #titulo
        st.subheader("Visão gerão da divisão dos cluster. Temos 5 cluster identificados com caracteristicas distintas")
        
        # agrupando os cluster para plotar no grafico de barras
        df_res = df_norm.groupby('cluster',as_index=False).mean()
        #df_res.columns
        if (selecao):
            fig = px.bar(df_res, x="cluster", y=selecao, title="Wide-Form Input")
        else:
            fig = px.bar(df_res, x="cluster", y=df_res.columns, title="Wide-Form Input")
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=False,height=400,width=1400)
        st.write(fig)



    with cluster0:

        st.subheader("Cluster 0:")
        st.markdown("**Caracteristica:** Grande empresas com alto score de pontualidade e uma consideravel margem bruta acumulada. ")
        st.write("")
        st.write("")
        col1, col2 = st.columns([1,1.2])
# grafico de barra
        medias =  df_norm[ df_norm.cluster== 0].mean()
        medias.drop(['cluster'], inplace = True)

        df_medias=pd.DataFrame(medias)
        #
        fig0 = px.bar(df_medias, x=df_medias.columns, title="Cluster 0")
        fig0.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=True)
        col1.write(fig0)
# grafico de radar
        colnames = df_norm.drop(['cluster'], axis = 1).columns

        fig00 = px.line_polar(medias,r=medias.values , theta= colnames, line_close=True)
        fig00.update_traces(fill='toself')
        col2.write(fig00)

    with cluster1:

        st.subheader("Cluster 1:")
        st.markdown("**Caracteristica:** Apenas empresas pequenas empresas com score de pontualidade alto.")
        st.write("")
        st.write("")
        col1, col2 = st.columns([1,1.2])
# grafico de barra
        medias =  df_norm[ df_norm.cluster== 1].mean()
        medias.drop(['cluster'], inplace = True)

        df_medias=pd.DataFrame(medias)

        fig0 = px.bar(df_medias, x=df_medias.columns, title="Cluster 1")
        fig0.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=True)
        col1.write(fig0)
# grafico de radar
        colnames = df_norm.drop(['cluster'], axis = 1).columns
        fig00 = px.line_polar(medias,r=medias.values , theta= colnames, line_close=True)
        fig00.update_traces(fill='toself')
        col2.write(fig00)

    with cluster2:

        st.subheader("Cluster 2:")
        st.markdown("**Caracteristica:** Apenas pequenas empresas com baixo score de pontualidade e com algumas restrições.")
        st.write("")
        st.write("")
        col1, col2 = st.columns([1,1.2])
# grafico de barra
        medias =  df_norm[ df_norm.cluster== 2].mean()
        medias.drop(['cluster'], inplace = True)

        df_medias=pd.DataFrame(medias)

        fig0 = px.bar(df_medias, x=df_medias.columns, title="Cluster 2")
        fig0.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=True)
        col1.write(fig0)
# grafico de radar
        colnames = df_norm.drop(['cluster'], axis = 1).columns
        fig00 = px.line_polar(medias,r=medias.values , theta= colnames, line_close=True)
        fig00.update_traces(fill='toself')
        col2.write(fig00)

    with cluster3:

        st.subheader("Cluster 3:")
        st.markdown("**Caracteristica:** Grandes empresas com baixo score de pontualidade e indice de dashboard alto e com definição de risco médio.")
        st.write("")
        st.write("")
        col1, col2 = st.columns([1,1.2])
# grafico de barra
        medias =  df_norm[ df_norm.cluster== 3].mean()
        medias.drop(['cluster'], inplace = True)

        df_medias=pd.DataFrame(medias)

        fig0 = px.bar(df_medias, x=df_medias.columns, title="Cluster 3")
        fig0.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=True)
        col1.write(fig0)
# grafico de radar
        colnames = df_norm.drop(['cluster'], axis = 1).columns
        fig00 = px.line_polar(medias,r=medias.values , theta= colnames, line_close=True)
        fig00.update_traces(fill='toself')
        col2.write(fig00)


    with cluster4:

        st.subheader("Cluster 4:")
        st.markdown("**Caracteristica:** Clientes com restrições e com alto score de pontualidade.")
        st.write("")
        st.write("")
        col1, col2 = st.columns([1,1.2])
# grafico de barra
        medias =  df_norm[ df_norm.cluster== 4].mean()
        medias.drop(['cluster'], inplace = True)

        df_medias=pd.DataFrame(medias)

        fig0 = px.bar(df_medias, x=df_medias.columns, title="Cluster 4")
        fig0.update_layout(margin=dict(l=0, r=0, b=0, t=0),autosize=True)
        col1.write(fig0)
# grafico de radar
        colnames = df_norm.drop(['cluster'], axis = 1).columns
        fig00 = px.line_polar(medias,r=medias.values , theta= colnames, line_close=True)
        fig00.update_traces(fill='toself')
        col2.write(fig00)