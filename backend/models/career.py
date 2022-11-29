from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import declarative_base
from config.database import Base


class Career(Base):
    __tablename__ = 'careers'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    page_url = Column(String(250))
    university_id = Column(Integer, ForeignKey('universities.id'))

    def __repr__(self) -> str:
        return f"Career(id={self.id}, name={self.name}, url={self.page_url})"
