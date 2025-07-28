from pydantic import BaseModel
from typing import Optional, Dict

# Base commune à la création, lecture, update
class GoalBase(BaseModel):
    title: str
    description: Optional[str]
    category: Optional[str]
    total_days: int
    selected_month: str

class GoalCreate(GoalBase):
    pass

class GoalUpdateProgress(BaseModel):
    day: int
    value: bool

class Goal(GoalBase):
    id: str
    user_id: int
    progress: Dict[int, bool]

    class Config:
        orm_mode = True  # Pour la compatibilité SQLAlchemy -> Pydantic