import streamlit as st
from controller import ItemController 


st.set_page_config(page_title="Listagem de itens", layout="centered")
st.title("📝 Lista de itens")

st.header("Inserir um novo item")
with st.form(key="new_item_form", clear_on_submit=True):
    objeto = st.text_input('Objeto')
    descricao = st.text_input("Descrição")
    quantidade = st.text_input("Quantidade")
    submit_button = st.form_submit_button(label="Inserir")

if submit_button:
    ItemController.add_new_item(objeto, descricao, quantidade)
    st.rerun() 

st.markdown("---")

st.header("Itens inseridos recentemente")

all_itens = ItemController.get_all_itens()

if not all_itens:
    st.info("Nenhum item foi inserido ainda.")
else:
    for item in all_itens:
        st.subheader(item.objeto)
        st.write(f"Quantidade: {item.quantidade}")
        st.write(item.descricao)
        st.markdown("---")