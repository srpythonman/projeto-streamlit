import streamlit as st
import pandas as pd
import datetime

data_min = datetime.date(1900, 1, 1)
data_max = datetime.date(2100, 12, 31)

def  gravar_dados(nome, dt_nasc, natureza_juridica):
    if nome and dt_nasc <= datetime.date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {dt_nasc}, {natureza_juridica}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.set_page_config(
    page_title="Cadastro de clientes", 
    page_icon="🧾"
)

st.title("Cadastro de clientes")
st.divider()


nome = st.text_input("Digite o nome do cliente", 
                     key="nome_cliente"
)

dt_nasc = st.date_input("Data de nascimento",value=datetime.date(2024, 7, 23), min_value=data_min, max_value=data_max, format="DD/MM/YYYY")

natureza_juridica = st.selectbox("Tipo do cliente", ["Pessoa física", "Pessoa jurídica"])

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=[nome, dt_nasc, natureza_juridica])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", 
                   icon="✔")
    else:
        st.error("Houve um erro no cadastro", 
                   icon="❌")
