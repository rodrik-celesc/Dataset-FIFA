import streamlit as st
import pandas as pd
from datetime import datetime

# config
st.set_page_config(
    
    layout="wide", 
    page_title="Home",
    page_icon="⭐",
    initial_sidebar_state="expanded"
    
)

# titulo
st.markdown("# FIFA DATASET! ⚽")

# assinatura
st.sidebar.markdown("Desenvolvido por :blue[RodriK]")

# corpo do texto
st.markdown(
    """
    O dataset **FIFA 2023** disponível no Kaggle contém informações detalhadas sobre jogadores de futebol, 
    times e estatísticas do jogo. Ele inclui atributos como habilidades, posições, idades, 
    nacionalidades e valores de mercado dos jogadores, além de dados sobre ligas e clubes. 
    Este conjunto de dados é frequentemente utilizado para análises estatísticas, 
    visualizações e para treinos em projetos de machine learning relacionados ao futebol. 
    É uma excelente fonte para quem deseja explorar o desempenho dos jogadores e 
    entender as dinâmicas do futebol profissional.
    """
)

# carregar dados
@st.cache_data
def carregar_dados():
    
    # importar
    df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    
    # excluir jogadores sem registro de valor
    df = df[df["Value(£)"] > 0]
    
    # ordenar
    df = df.sort_values(by="Overall", ascending=False)
    
    return df

    
# atribuir df a session state dados
dados = carregar_dados()
st.session_state["dados"] = dados
    
import os
os.getcwd()

