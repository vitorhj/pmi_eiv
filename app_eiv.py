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
     page_title="PMI - Empresas Alvará de Funcionamento",
     page_icon=('./dados/favicon.png'),
     layout="wide",
 )

#______________________________________________________________________________________________________________________
