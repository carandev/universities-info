from fastapi import APIRouter
from sqlalchemy import select
from models.career import Career
from scraper.main import careers_to_db
from models.university import University
from sqlalchemy.orm import Session
from config.database import db_engine
university = APIRouter()


@university.get("/universities")
def get_universities():
    with Session(db_engine) as session:
        return session.execute(select(University)).fetchall()


@university.get("/universities/update")
def update_universities():
    careers_to_db()
    return "OK"


@university.get("/universities/{university_id}")
def get_university(university_id: int):
    with Session(db_engine) as session:
        return session.execute(select(University).where(University.id == university_id)).fetchall()


@university.get("/universities/{university_id}/careers")
def get_career(university_id: int):
    with Session(db_engine) as session:
        return session.execute(select(Career).where(Career.university_id == university_id)).fetchall()
