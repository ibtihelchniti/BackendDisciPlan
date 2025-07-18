from pydantic import BaseModel
from typing import List, Literal

class WeeklyGoal(BaseModel):
    id: int | None = None
    title: str
    days_status: List[Literal['done', 'not_done']]  # 7 éléments: pour chaque jour de la semaine