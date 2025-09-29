import streamlit as st
from controller import ItemController 
from setup_database import cursor


st.set_page_config(page_title="Lista de itens", layout="centered")
st.title("📝 Listagem de itens")

st.header("Inserir um novo item")
with st.form(key="new_item_form", clear_on_submit=True):
    nome = st.text_input('Nome')
    descricao= st.text_input("Descrição")
    quantidade = st.text_input("Quantidade")
    submit_button = st.form_submit_button(label="inserir")

if submit_button:
    ItemController.add_new_item(nome, descricao, quantidade)
    st.rerun() 
st.markdown("---")


st.header("Itens recentemente adicionados")

all_itens = ItemController.get_all_itens()

if not all_itens:
    st.info("Ainda não há itens listados.")
else:
    for item in all_itens:
        st.subheader(item.nome)
        st.text(f'Quantidade: {item.quantidade}')
        st.text(item.descricao)
        st.markdown("---")