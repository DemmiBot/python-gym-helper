import streamlit as st
import pandas as pd
import plotly_express as px

#Dados
treino_df = pd.read_csv("dados_de_treino.csv", delimiter=";")
treino_df["dia"] = pd.to_datetime(treino_df["dia"], format="%d/%m/%Y")
treino_df["dia_convertido"] = treino_df["dia"].dt.strftime("%d/%m/%Y")
range = st.sidebar.select_slider("Período (Filtra somente carga):", treino_df["dia_convertido"].unique(), (treino_df["dia_convertido"].iloc[0], treino_df["dia_convertido"].iloc[-1]))
treino_df["exercicios"] = treino_df["nome_exercicio"] + treino_df["treino"]
treino_filtered = treino_df[(pd.to_datetime(range[0], format="%d/%m/%Y") <= treino_df["dia"]) & (treino_df["dia"] <= pd.to_datetime(range[1], format="%d/%m/%Y"))]



#Renderização
st.write("# Carga dos exercicios")
st.write("Essas são as cargas que você anotou durante os dias em que você se exercitou. Os gráficos são interativos, você pode testar clicando e arrastando o mouse pelo gráfico, ou utilizando as opções padrão. caso você não esteja vendo nenhum treino, você precisa executar o app de treinos e inserir um novo treino!")

exercicios = treino_df["exercicios"].unique().tolist()
exercicios_df = []

cols = st.columns(6)

for e in exercicios:
    exercicios_df.append(treino_filtered[treino_filtered["exercicios"] == e])

charts = []

for df in exercicios_df:
    w_day = df["treino"].iloc[0]
    current = px.bar(df,
                         labels={"dia_convertido": "", "carga": df["tipo_de_carga"].iloc[0].title()},
                         title=df["nome_exercicio"].iloc[0] + " (" + df["treino"].iloc[0] + ")",
                         x="dia_convertido",
                         y="carga",
                         color_discrete_sequence=["royalblue" if w_day == 'a' else "darkturquoise" if w_day == 'b' else "mediumslateblue" if w_day == 'c' else "tomato" if w_day == 'd' else "lightseagreen"],
                         width=300,
                         height=300,)
    # current.update_yaxes(range=[0, 200])
    charts.append(current)

for i, chart in enumerate(charts):
    cols[i%6].plotly_chart(chart)