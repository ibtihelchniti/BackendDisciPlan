from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from db import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String)
    total_days = Column(Integer)
    selected_month = Column(String)  # Ex: "2024-07"
    progress = Column(JSON, default={})  # Format : {"1": true, "2": false, ...}