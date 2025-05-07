from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class ScheduleRequest(BaseModel):
    teachers: List[str]
    periods: int

@app.post("/schedule")
def generate_schedule(data: ScheduleRequest) -> Dict[str, List[str]]:
    schedule = {}
    for i, teacher in enumerate(data.teachers):
        schedule[teacher] = [f"Period {p}" for p in range(i, data.periods, len(data.teachers))]
    return {"schedule": schedule}