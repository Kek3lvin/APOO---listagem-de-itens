from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Item:
    nome: str
    descricao: str
    quantidade: int
    id: Optional[int] = None