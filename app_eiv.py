#______________________________________________________________________________________________________________________

## IMPORTA BIBLIOTECAS PARA O PYTHON ##

import pandas as pd
import re
import streamlit as st
import os
from PIL import Image

#______________________________________________________________________________________________________________________

## CONFIGURAÇÃO DA PÁGINA DO STREAMLIT ##

st.set_page_config(
     page_title="PMI - EIV",
     page_icon=('./dados/favicon.png'),
     layout="wide",
 )

#______________________________________________________________________________________________________________________

## SIDEBAR ##

# Input box do aprova
logo_image = ('./dados/logo.png')
st.sidebar.image(logo_image, width=200)
st.sidebar.subheader('Verificação EIV:')

inscricao_input = st.sidebar.text_input('Inscrição Imobiliária:','',key="inputbox_inscricao")
cnpj_input = st.sidebar.text_input('CTRL + V do CNPJ:','',key="inputbox_cnpj")

#_____________________________________________________________________________________________________________________

## BOTÃO LIMPAR ##

def clear_text():
    st.session_state["inscricao_input"] = ""
    st.session_state["cnpj_input"] = ""
    st.session_state["areatotal_input"] = ""
    st.session_state["areaconstruida_input"] = ""
st.sidebar.button("Limpar", on_click=clear_text)

#______________________________________________________________________________________________________________________

## INPUTBOX CNPJ ##

if cnpj_input != "":
    cnaes_cnpj_input = re.findall(r'\d\d.\d\d-\d-\d\d', cnpj_input)
    cnae_principal_cnpj_input=cnaes_cnpj_input[0]
    numero_cnpj_input = re.findall(r'\d\d.\d\d\d.\d\d\d/\d\d\d\d-\d\d', cnpj_input)

    texto_cnpj_split = re.sub(' +', ' ',cnpj_input).split(' ')

    #Separa o cartão cnpj em elementos separado por espaços para extração de textos específicos
    itens_analise=['EMPRESARIAL','TÍTULO', 'LOGRADOURO','NÚMERO']
    index_cnpj1=texto_cnpj_split.index('EMPRESARIAL')+1
    index_cnpj2=texto_cnpj_split.index('TÍTULO')
    razao_social_cnpj2 = " ".join(texto_cnpj_split[index_cnpj1:index_cnpj2])

    #Separa o primeiro split para puxar o endereço
    index_cnpj3=texto_cnpj_split.index('NATUREZA')+1
    index_cnpj4=texto_cnpj_split.index('ESPECIAL')
    texto_cnpj_split = texto_cnpj_split[index_cnpj3:index_cnpj4] #função que separa o primeiro split
    
    index_cnpj5=texto_cnpj_split.index('LOGRADOURO')+1
    index_cnpj6=texto_cnpj_split.index('NÚMERO')
    logradouro_cnpj2 = " ".join(texto_cnpj_split[index_cnpj5:index_cnpj6])
    index_cnpj7=texto_cnpj_split.index('NÚMERO')+1
    index_cnpj8=texto_cnpj_split.index('COMPLEMENTO')
    numeropredial_cnpj2 = " ".join(texto_cnpj_split[index_cnpj7:index_cnpj8])
    index_cnpj9=texto_cnpj_split.index('COMPLEMENTO')+1
    index_cnpj10=texto_cnpj_split.index('CEP')
    complemento_cnpj2 = " ".join(texto_cnpj_split[index_cnpj9:index_cnpj10])
    index_cnpj11=texto_cnpj_split.index('BAIRRO/DISTRITO')+1
    index_cnpj12=texto_cnpj_split.index('MUNICÍPIO')
    bairro_cnpj2 = " ".join(texto_cnpj_split[index_cnpj11:index_cnpj12])

else:
   razao_social_cnpj2 = ""

#_____________________________________________________________________________________________________________________

## PÁGINA CENTRAL - RESULTADO DA VERIFICAÇÃO ##

st.title('PMI - EIV')
if (inscricao_input or cnpj_input) == '':
        st.markdown('Aplicação web destinada à verificação da necessidade de estudo de impacto de vizinhança (EIV) em empresas.')

        st.subheader('Tabelas com os parâmetros adotados na verificação da necessidade de EIV:')
        st.markdown('Anexo EIV: '+str('https://docs.google.com/spreadsheets/d/1vwx3hPDPmSIU-N1KE2iXfstt-ZH1jGQhhz0ZPNrA-vY/edit#gid=0'))
        st.markdown('Inscrição e Zoneamento: '+str('https://docs.google.com/spreadsheets/d/1cMTb_8sICzDvanbFVCDvez-S4McgoLaVvbAQeDMSidY/edit#gid=0'))
        st.markdown('CNAES e usos: '+str('https://docs.google.com/spreadsheets/d/1FhBwkTrFslht9ORzra1WcI1-BfqIw5EBTZjWzeitzTw/edit#gid=200488863'))
     
try:    
        tabela_inscricao = pd.read_csv('./dados/inscricao_zoneamento.csv', sep=',')
        tabela_cnaes = pd.read_csv('./dados/cnaes-ibge_uso-atividades.csv', sep=',')
        tabela_anexoeiv = pd.read_csv('./dados/anexo_eiv.csv', sep=',')
        
        tabela_cnaes_cnpj = pd.DataFrame(cnaes_cnpj_input)
        
        st.subheader('Dados:')         
        inscricao15 = inscricao_input[0:15]
        inscricao15=str(inscricao15)
        inscricao15
        tabela_filtrada = tabela_inscricao[tabela_inscricao.inscricao==inscricao15]
        tabela_filtrada
          
        st.subheader('CNAE e classificação de uso:')
        tabela_parametros_uso = tabela_cnaes.merge(tabela_cnaes_cnpj,left_on='CÓDIGO', right_on=0)
        tabela_parametros_uso.drop([0], axis=1, inplace=True)
        tabela_parametros_uso
        
        tabela_inscricao
        tabela_anexoeiv
        

     

        #inscricao15 = pd.DataFrame(inscricao15)
        #inscricao15
     

        
        #15 primeiros dígitos da inscrição imobiliária
        #tabela_inscricao = pd.DataFrame(inscricao_input[1:15])
        #tabela_zona = tabela_inscricao.merge(inscricao_input[1:15],left_on='inscricao', right_on=0)
        
except:
  pass
