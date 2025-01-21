import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

pessoa = pd.read_csv("dados_pessoa.csv", delimiter=";")

st.sidebar.markdown("# Dados pessoais")
st.sidebar.markdown(" **Nome do aluno:** " + pessoa["nome"].iloc[0])
st.sidebar.markdown(" **Idade:** " + str(pessoa["idade"].iloc[0]))
st.sidebar.markdown(" **Altura:** " + str(pessoa["altura"].iloc[0]) + " cm")

st.sidebar.markdown("# Analisador de treino pessoal")
st.sidebar.markdown("Para se exercitar de forma adequada, é importante conhecer os indicadores de saúde relevantes, assim como as cargas que você consegue utilizar em cada exercício praticado, para planejar e executar a progressão do treino. Você pode ignorar os dados pessoais e de saúde, no entanto é recomendado anotar a progressão de carga, para garantir que há progresso de força e ajustar de acordo.")

pages = st.navigation([
    st.Page("gymapp.py", title="Exercícios e carga"),
    st.Page("saude.py", title="Saúde")
])
pages.run()