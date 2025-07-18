from fastapi import APIRouter
from models.weekly_goal import WeeklyGoal

router = APIRouter()

goals: list[WeeklyGoal] = []

@router.post("/weekly-goals")
def create_weekly_goal(goal: WeeklyGoal):
    goal.id = len(goals) + 1
    goals.append(goal)
    return goal

@router.get("/weekly-goals")
def get_weekly_goals():
    return goals

@router.put("/weekly-goals/{goal_id}")
def update_weekly_goal(goal_id: int, goal: WeeklyGoal):
    for g in goals:
        if g.id == goal_id:
            g.title = goal.title
            g.days_status = goal.days_status
            return g
    return {"error": "Goal not found"}
