from fastapi import FastAPI
from routes import monthly_goal, weekly_goal

app = FastAPI()

# Inclure les routes
app.include_router(monthly_goal.router)
app.include_router(weekly_goal.router)

@app.get("/")
def root():
    return {"message": "DisciPlan API is running"}
