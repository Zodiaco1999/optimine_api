from typing import List

from pydantic import BaseModel

class Replacement(BaseModel):
    part_number: str
    label: str
    quantity: int
    name: str

known_replacements: List[Replacement] = [
    Replacement(
        part_number="123-ABC",
        label="0 vaso",
        quantity=11,
        name="Vaso Ejemplo"
    ),
    Replacement(
        part_number="456-DEF",
        label="1 estuche",
        quantity=12,
        name="Estuche Ejemplo"
    )
]
