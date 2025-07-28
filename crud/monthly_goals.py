from sqlalchemy.orm import Session
from models.monthly_goals import Goal
from schemas.monthly_goals import GoalCreate
import uuid

# Création d'un objectif
def create_goal(db: Session, user_id: int, goal: GoalCreate) -> Goal:
    db_goal = Goal(
        id=str(uuid.uuid4()),
        user_id=user_id,
        **goal.dict(),
        progress={}
    )
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

# Récupération des objectifs d'un mois
def get_goals(db: Session, user_id: int, month: str) -> list[Goal]:
    return db.query(Goal).filter_by(user_id=user_id, selected_month=month).all()

# Mise à jour du suivi jour par jour
def update_progress(db: Session, goal_id: str, day: int, value: bool) -> Goal | None:
    goal = db.query(Goal).filter_by(id=goal_id).first()
    if not goal:
        return None
    goal.progress[str(day)] = value
    db.commit()
    db.refresh(goal)
    return goal