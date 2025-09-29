from typing import List
import streamlit as st  
from model import Item
from database import ItemDAO

class ItemController:

    dao = ItemDAO()
    
    @staticmethod
    @st.cache_data 
    def get_all_itens() -> List[Item]:

        return ItemController.dao.fetch_all_itens()

    @staticmethod
    def add_new_item(objeto: str, descricao: str, quantidade: str):

        if not descricao:
            st.error("Deve haver uma descrição")
            return

        new_item = Item(objeto=objeto, descricao=descricao, quantidade=quantidade)
        
        ItemController.dao.add_item(new_item)
        
        st.cache_data.clear()