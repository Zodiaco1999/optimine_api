from pydantic import BaseModel
from typing import Optional
from models.replacement import Replacement


class PredictResponse(BaseModel):
    confidence_score: float
    replacement: Optional[Replacement]
    is_success: bool