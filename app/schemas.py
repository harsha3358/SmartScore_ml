from pydantic import BaseModel

class StudentInput(BaseModel):
    study_hours: float
    sleep_hours: float
    screen_time: float
    attendance: float
    practice_tests: float