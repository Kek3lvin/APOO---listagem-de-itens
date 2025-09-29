from typing import List
import streamlit as st 

from model import Item
from database import ItemDAO

class ItemController:
    """
    Classe controladora para gerenciar as operações de posts.
    Ela conecta a View (app.py) com o Model (Item) e o DAL (ItemDAO.py).
    """
    dao = ItemDAO()
    
    @staticmethod
    @st.cache_data 
    def get_all_itens() -> List[Item]:
        return ItemController.dao.fetch_all_itens()

    @staticmethod
    def add_new_item(nome: str, descricao: str, quantidade: int):
  
        if len(descricao) < 5:
            st.error("A descrição deve ter no mínimo 5 caracteres.")
            return

        new_item = Item(nome=nome, descricao=descricao, quantidade=quantidade)
        

        ItemController.dao.add_item(new_item)
        
        st.cache_data.clear()