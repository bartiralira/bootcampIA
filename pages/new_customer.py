import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor as rfr
import joblib
import streamlit as st



def app():
    #st.markdown("## Novo cliente")
    # deixa a pagina full wide
    #st.set_page_config(layout="wide")
    #app = MultiPage()

    # preparando a sepracao da pagina
    header = st.container()
    novo_cluster = st.container()
    sugestao_limite = st.container()

    modelo = joblib.load("./modelo/classificador_cliente.pkl")


    # comeca os containers
    @st.cache
    def get_data(filename):
        file= pd.read_csv(filename,sep="\t",decimal='.', engine='python')
        file = file.reindex(sorted(file.columns), axis=1)
        file.drop(file.columns[0],inplace=True,axis=1)
        file.drop(["cluster"],inplace=True,axis=1)
        return file

    with header:
        st.title("Adicionando novo cliente:")
        df = get_data('./data/datasetclusterizado.csv')   
    
    with novo_cluster: 
        form = st.form(key='my_form')
        #cnpjSemTraco = form.number_imput("CNPJ (sem traço)")
        ativoCirculante = form.number_input("Ativo Circulante", format="%.2f")
        capitalSocial = form.number_input('Capital Social', format="%.2f")
        custos = form.number_input('Custos', format="%.2f")
        dashboardCorrelacao=form.slider('Dashboard Correlação',-10.0,10.0,0.0)
        definicaoRisco=form.slider('Definição de risco',0, 4,0)
        empresa_MeEppMei= (1 if form.radio("Empresa ME/MEI/EPP",("Sim","Não"))=="Sim" else 0)
        endividamento = form.number_input('Endividamento', format="%.2f")
        estoque = form.number_input('Estoque', format="%.2f")
        faturamentoBruto = form.number_input('Faturamento Bruto', format="%.2f")
        limiteEmpresaAnaliseCredito = form.number_input('Analise de Crédito', format="%.2f")
        maiorAtraso=form.slider('Mario atraso(dias)',0, 1000)
        margemBruta = form.number_input('Margem bruta', format="%.2f")
        margemBrutaAcumulada = form.number_input('Margem bruta acumulada', format="%.2f")
        passivoCirculante = form.number_input('Passivo circulante', format="%.2f")
        percentualProtestos=form.slider('Percentual de protestos (%)',0, 100)
        prazoMedioRecebimentoVendas=form.slider('Prazo médio de recebimento de vendas',0, 1000)
        restricoes=(1 if form.radio('Restrições',("Sim","Não")) == "Sim" else 0)
        scorePontualidade=form.slider('Score de pontualidade',0.0, 1.0)
        titulosEmAberto = form.number_input('Títulos em aberto', format="%.2f")
        totalPatrimonioLiquido = form.number_input('Patrimonio líquido', format="%.2f")
        valorAprovado = form.number_input('Valor aprovado', format="%.2f")
        valorSolicitado = form.number_input('Valor solicitado', format="%.2f")
        cluster_button = form.form_submit_button(label='Cluster Indicado')


    with novo_cluster:
        if cluster_button:
            dd=[[ativoCirculante,capitalSocial,custos,dashboardCorrelacao,definicaoRisco,empresa_MeEppMei,endividamento,
            estoque,faturamentoBruto,limiteEmpresaAnaliseCredito,maiorAtraso,margemBruta,margemBrutaAcumulada,
            passivoCirculante,percentualProtestos,prazoMedioRecebimentoVendas,restricoes,scorePontualidade,titulosEmAberto,totalPatrimonioLiquido,valorAprovado,valorSolicitado]]
            df_new=pd.DataFrame(dd)
            df_new.columns = df.columns
            cluster_indicado1 = modelo.predict(df_new)
            cluster_indicado = str(modelo.predict(df_new))
            if cluster_indicado == "[0]":
                cluster_label = "Cluster 0 - Grandes empresas e pontual"
            elif cluster_indicado == "[1]":
                cluster_label = "Cluster 1 - Pequenas empresas e pontual"
            elif cluster_indicado == "[2]":
                cluster_label = "Cluster 2 - Pequenas empresas sem pontualidade."
            elif cluster_indicado == "[3]":
                cluster_label = "Cluster 3 - Grandes empresas sem pontualidade"
            elif cluster_indicado == "[4]":
                cluster_label = "Cluster 4 - Empresas (grandes e pequenas) pontuais mas com restrição"
           
            #st.write(f'O cliente é indicado para o cluster: {cluster_indicado1}')
            st.markdown(f'O cliente é indicado para o cluster: **{cluster_label}**')
            #st.write(empresa_MeEppMei)
