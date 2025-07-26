from dataclasses import * 
@dataclass
class Cookie: 
    name: str
    quantity: int = 0
    
    
emperador = Cookie("Emperador de Nuez", 12)
print(emperador)