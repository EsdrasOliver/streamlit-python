import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu site Streamlit")

with st.container():
    st.write("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informacoes sobre os contratos fechados pela empresa tal ao longo de maio")
    st.write("Quer documentacao do Streamlit? [Clique aqui](https://docs.streamlit.io/get-started)")

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv")
    return tabela

with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o periodo", ["7D", "15D", "21D", "30D"])
    num_dias = int(qtde_dias.replace("D", ""))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")