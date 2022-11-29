from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import declarative_base, relationship
from config.database import Base


class University(Base):
    __tablename__ = 'universities'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    page_url = Column(String(250))
    careers = relationship("Career")

    def __repr__(self) -> str:
        return f"id={self.id}, name={self.name}, url={self.page_url}"
