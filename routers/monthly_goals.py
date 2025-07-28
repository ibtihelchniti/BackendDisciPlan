from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.monthly_goals import GoalCreate, GoalUpdateProgress, Goal
from crud import monthly_goals as crud_goal
from db import get_db
from auth.utils import get_current_user

router = APIRouter()

@router.post("/goals/", response_model=Goal)
def create_goal(goal: GoalCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    return crud_goal.create_goal(db, user_id, goal)

@router.get("/goals/", response_model=list[Goal])
def get_goals(month: str, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    goals = crud_goal.get_goals(db, user_id, month)
    if goals is None:
        raise HTTPException(status_code=404, detail="Goals not found")
    return goals

@router.patch("/goals/{goal_id}/progress")
def update_progress(goal_id: str, update: GoalUpdateProgress, db: Session = Depends(get_db)):
    updated_goal = crud_goal.update_progress(db, goal_id, update.day, update.value)
    if updated_goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return updated_goal