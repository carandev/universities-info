from sqlalchemy.orm import Session
from fastapi import APIRouter
from config.database import db_engine
from sqlalchemy import select
from models.career import Career
from models.subject import Subject


career = APIRouter()


@career.get("/careers/{career_id}")
def get_career(career_id: int):
    with Session(db_engine) as session:
        return session.execute(select(Career).where(Career.id == career_id)).fetchone()


@career.get("/careers/{career_id}/subjects")
def get_career_subjects(career_id: int):
    with Session(db_engine) as session:
        return session.execute(select(Subject).where(Subject.career_id == career_id)).fetchall()


@career.get("/careers")
def get_careers():
    with Session(db_engine) as session:
        return session.execute(select(Career)).fetchall()
