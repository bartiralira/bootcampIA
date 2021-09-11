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

    modelo = joblib.load("./modelo/indicacao_valor_maximo.pkl")


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
        maiorAtraso=form.slider('Maior atraso(dias)',0, 1000)
        margemBruta = form.number_input('Margem bruta', format="%.2f")
        margemBrutaAcumulada = form.number_input('Margem bruta acumulada', format="%.2f")
        passivoCirculante = form.number_input('Passivo circulante', format="%.2f")
        percentualProtestos=form.slider('Percentual de protestos (%)',0, 100)
        prazoMedioRecebimentoVendas=form.slider('Prazo médio de recebimento de vendas',0, 1000)
        restricoes=(1 if form.radio('Restrições',("Sim","Não")) == "Sim" else 0)
        scorePontualidade=form.slider('Score de pontualidade',0.0, 1.0)
        titulosEmAberto = form.number_input('Títulos em aberto', format="%.2f")
        totalPatrimonioLiquido = form.number_input('Patrimonio líquido', format="%.2f")
        #valorAprovado = form.number_input('Valor aprovado', format="%.2f")
        valorSolicitado = form.number_input('Valor solicitado', format="%.2f")
        valor_sugerido_button = form.form_submit_button(label='Valor máximo indicado')


    with sugestao_limite:
        if valor_sugerido_button:
            new_valor=[[ativoCirculante,capitalSocial,custos,dashboardCorrelacao,definicaoRisco,empresa_MeEppMei,endividamento,
            estoque,faturamentoBruto,limiteEmpresaAnaliseCredito,maiorAtraso,margemBruta,margemBrutaAcumulada,
            passivoCirculante,percentualProtestos,prazoMedioRecebimentoVendas,restricoes,scorePontualidade,titulosEmAberto,totalPatrimonioLiquido,valorSolicitado]]
            df_valor=pd.DataFrame(new_valor)
            #df_valor.columns = df.columns

            #fazendo a predição
            #valor = clf.predict(df_valor.iloc[:, new_dd.columns != 'valorAprovado'])

            #df_valor=pd.DataFrame(df_valor)
            #df_valor.columns = df.columns
            #valor_indicado =modelo.predict(df_valor.iloc[:, df_valor.columns != 'valorAprovado'])
            valor_indicado =modelo.predict(new_valor)

            #imprimindo valor sugerido na tela
            st.write(f'Valor máximo indicado: {valor_indicado}')