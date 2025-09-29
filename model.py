from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Item:
    objeto: str
    quantidade: str
    descricao: str
    id: Optional[int] = None
