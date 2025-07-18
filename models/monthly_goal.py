from pydantic import BaseModel
from typing import List

class MonthlyGoal(BaseModel):
    id: int | None = None  # auto-généré côté DB
    title: str
    description: str
    achieved: bool = False