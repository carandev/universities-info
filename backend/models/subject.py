from sqlalchemy import Integer, String, Column, ForeignKey
from config.database import Base


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    file_url = Column(String(250))
    semester = Column(Integer)
    career_id = Column(Integer, ForeignKey('careers.id'))

    def __repr__(self) -> str:
        return f"Subject(id={self.id}, name={self.name}, url={self.file_url}, semester={self.semester})"
