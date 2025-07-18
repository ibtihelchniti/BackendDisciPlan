from fastapi import APIRouter
from models.monthly_goal import MonthlyGoal

router = APIRouter()

# simulation en mémoire pour commencer
goals: list[MonthlyGoal] = []

@router.post("/monthly-goals")
def create_goal(goal: MonthlyGoal):
    goal.id = len(goals) + 1
    goals.append(goal)
    return goal

@router.get("/monthly-goals")
def list_goals():
    return goals

@router.put("/monthly-goals/{goal_id}")
def update_goal(goal_id: int, goal: MonthlyGoal):
    for g in goals:
        if g.id == goal_id:
            g.title = goal.title
            g.description = goal.description
            g.achieved = goal.achieved
            return g
    return {"error": "Goal not found"}

@router.delete("/monthly-goals/{goal_id}")
def delete_goal(goal_id: int):
    global goals
    goals = [g for g in goals if g.id != goal_id]
    return {"status": "deleted"}
