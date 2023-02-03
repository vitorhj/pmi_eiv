#______________________________________________________________________________________________________________________

## IMPORTA BIBLIOTECAS PARA O PYTHON ##

import pandas as pd
import re
import streamlit as st
import os
from PIL import Image

#______________________________________________________________________________________________________________________

## INPUTS DA PÁGINA DO STREAMLIT ##

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
areatotal_input = st.sidebar.text_input('Área total (m²):','',key="inputbox_areatotal")
areaconstruida_input = st.sidebar.text_input('Área construída (m²):','',key="inputbox_areaconstruida")
