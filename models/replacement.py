from typing import List

from pydantic import BaseModel

class Replacement(BaseModel):
    part_number: str
    label: str
    quantity: int
    name: str

known_replacements: List[Replacement] = [
    Replacement(
        part_number="4400454",
        label="0 Inyector de grasa",
        quantity=14,
        name="Inyector de grasa"
    ),
    Replacement(
        part_number="4400422",
        label="1 MANIPULADOR IZQUIERDO",
        quantity=12,
        name="Manipulador izquierdo"
    ),
    Replacement(
        part_number="4192035",
        label="2 SENSOR DE NIVEL DE GRASA",
        quantity=23,
        name="Sensor de nivel de grasa"
    ),
    Replacement(
        part_number="4400418",
        label="3 FILTRO DE AIRE ACONDICIONADO",
        quantity=9,
        name="Filtro de aire acondicionado"
    ),
    Replacement(
        part_number="4385019",
        label="4 MANGUERA",
        quantity=21,
        name="Manguera de alta bomba auxiliar"
    )
]
