from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from models.entrepreneur import Entrepreneurs

# инициализация декларативного стиля
Base = declarative_base()


class Business(Base):

    __tablename__ = 'business'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    entrepreneur_id = Column(Integer, ForeignKey('entrepreneurs.id'))
    entrepreneur = relationship(
        Entrepreneurs,
        backref=backref('entrepreneurs',
                        uselist=True,
                        cascade='delete-orphan, all'))

    def __str__(self):
        return self.name
