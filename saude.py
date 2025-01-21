import streamlit as st
import pandas as pd
import plotly_express as px

#Dados

saude = pd.read_csv("dados_saude.csv", delimiter=";")
saude["dia"] = pd.to_datetime(saude["dia"], format="%d/%m/%Y")
saude["dia_convertido"] = saude["dia"].dt.strftime("%d/%m/%Y")

cols = st.columns(3)

cols[0].write("# Estatísticas de saúde")
cols[0].write("Os principais medidores de saúde. Para adquirir os valores, você pode utilizar uma balança de bioimpedância.")

cols2 = st.columns(2)

left_cols = cols2[0].columns(3)
right_cols = cols2[1].columns(3)

#Peso e gordura
left_cols[1].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "peso": "Kg"}, title="Peso corporal", x="dia_convertido", y="peso", width=300, height=300).update_yaxes(range=[0,200]))
left_cols[0].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "g_braco_esq": "Kg"}, title="Gordura Braço Esquerdo", x="dia_convertido", y="g_braco_esq", width=300, height=300).update_yaxes(range=[0,20]))
left_cols[2].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "g_braco_dir": "Kg"}, title="Gordura Braço Direito", x="dia_convertido", y="g_braco_dir", width=300, height=300).update_yaxes(range=[0,20]))
left_cols[0].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "g_perna_esq": "Kg"}, title="Gordura Perna Esquerda", x="dia_convertido", y="g_perna_esq", width=300, height=300).update_yaxes(range=[0,20]))
left_cols[2].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "g_perna_dir": "Kg"}, title="Gordura Perna Direita", x="dia_convertido", y="g_perna_dir", width=300, height=300).update_yaxes(range=[0,20]))
left_cols[1].image("human-body-standing-up-free-vector.jpg", use_container_width=True)
left_cols[0].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "g_tronco": "Kg"}, title="Gordura Tronco", x="dia_convertido", y="g_tronco", width=300, height=300).update_yaxes(range=[0,20]))
left_cols[1].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "gordura_visceral": "Kg"}, title="Gordura visceral", x="dia_convertido", y="gordura_visceral", width=300, height=300).update_yaxes(range=[0,20]))
left_cols[2].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "gordura_subcutanea": "Kg"}, title="Gordura subcutânea", x="dia_convertido", y="gordura_subcutanea", width=300, height=300).update_yaxes(range=[0,30]))

#Massa magra e musculos
# right_cols[0].container(height=300, border=False)
# right_cols[2].container(height=300, border=False)
# right_cols[1].container(height=70, border=False)
right_cols[1].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "massa_magra": "Kg"}, title="Massa magra (Kg)", x="dia_convertido", y="massa_magra", width=300, height=300).update_yaxes(range=[0,200]))
right_cols[1].image("human-body-standing-up-free-vector.jpg", use_container_width=True)
right_cols[0].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "mm_braco_esq": "Kg"}, title="Musculo no braço esquerdo (Kg)", x="dia_convertido", y="mm_braco_esq", width=300, height=300).update_yaxes(range=[0,20]))
right_cols[2].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "mm_braco_dir": "Kg"}, title="Musculo no braço direito (Kg)", x="dia_convertido", y="mm_braco_dir", width=300, height=300).update_yaxes(range=[0,20]))
right_cols[0].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "mm_perna_esq": "Kg"}, title="Musculo na perna esquerda (Kg)", x="dia_convertido", y="mm_perna_esq", width=300, height=300).update_yaxes(range=[0,20]))
right_cols[0].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "mm_tronco": "Kg"}, title="Musculo no tronco (Kg)", x="dia_convertido", y="mm_tronco", width=300, height=300).update_yaxes(range=[0,20]))
right_cols[2].plotly_chart(px.bar(saude, labels={"dia_convertido": "", "mm_perna_dir": "Kg"}, title="Musculo na perna direita (Kg)", x="dia_convertido", y="mm_perna_dir", width=300, height=300).update_yaxes(range=[0,20]))