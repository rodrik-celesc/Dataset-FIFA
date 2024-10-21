import streamlit as st
import pandas as pd

# config
st.set_page_config(
    
    layout="wide", 
    page_title="Jogadores",
    page_icon="🏃‍♂️",
    initial_sidebar_state="expanded"
    
)

# importar dados
df = st.session_state["dados"]

# lista suspensa - lista de jogadores
jogadores = df["Name"].unique()
jogador = st.sidebar.selectbox("Jogador", jogadores)

# captura informações do jogador
info_jogador = df[df["Name"] == jogador].iloc[0]

# foto
st.image(info_jogador["Photo"])

# título
st.title(info_jogador["Name"])

# clube
coluna1, coluna2 = st.columns([0.05, 0.95])
coluna1.image(info_jogador["Club Logo"])
coluna2.markdown(f"**{info_jogador["Club"]}**")

# outras informações
coluna1, coluna2, coluna3, coluna4, = st.columns(4)
coluna1.markdown(f"**Idade:** {info_jogador["Age"]} anos")
coluna2.markdown(f"**Altura:** {info_jogador["Height(cm.)"]/100} metros")
coluna3.markdown(f"**Peso:** {info_jogador["Weight(lbs.)"]*0.453:.2f} Kg")
coluna4.markdown(f"**Nacionalidade:** {info_jogador["Nationality"]}")

# Ranking Melhor Jogador
st.subheader(f"Ranking: {info_jogador["Overall"]}")
st.progress(int(info_jogador["Overall"]))










