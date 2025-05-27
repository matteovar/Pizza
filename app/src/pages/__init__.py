from .page1 import visual
from .page2 import mapas
from .page3 import logistic
from .page4 import porce_map

# Dicionário com todas as páginas disponíveis
pages = {
    "General Informations": visual,
    "Geographic Distribution": mapas,
    "Customer Behavior": logistic,
    "Logistics and Delays": porce_map,
}
