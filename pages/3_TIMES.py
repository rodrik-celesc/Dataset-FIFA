import streamlit as st
import pandas as pd

# config
st.set_page_config(
    
    layout="wide", 
    page_title="Times",
    page_icon="⚽",
    initial_sidebar_state="expanded"
    
)

# importar dados
df = st.session_state["dados"]

# lista suspensa - lista de clubes
clubes = df["Club"].value_counts().index
clube = st.sidebar.selectbox("Clube", clubes)

# tabela
info_clube = df[df["Club"] == clube].set_index("Name")

# clube
st.image(info_clube.iloc[0]["Club Logo"])
st.markdown(f"### {info_clube.iloc[0]["Club"]}")

# tabela colunas
colunas_selecionadas = ["Age", "Nationality", "Flag", "Overall", "Club", "Value(£)", "Wage(£)", "Year_Joined", "Contract Valid Until"]
tabela_clube = info_clube[colunas_selecionadas]

# exibir tabela
st.dataframe(tabela_clube,
             column_config={
                 
                "Flag": st.column_config.ImageColumn("Flag"),
                "Overall": st.column_config.ProgressColumn("Overall", format="%d"),
                "Year_Joined": st.column_config.NumberColumn("Year_Joined", format="%d"),
                "Contract Valid Until": st.column_config.NumberColumn("Contract Valid Until", format="%d"),
                "Wage(£)": st.column_config.ProgressColumn("Wage(£)",
                                                           format="£%f",
                                                           min_value=0,
                                                           max_value=tabela_clube["Wage(£)"].max()
                                                           )
                 
                }
             
)