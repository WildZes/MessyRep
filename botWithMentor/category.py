from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

# инициализация декларативного стиля
Base = declarative_base()


class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    entrepreneur_id = Column(Integer, ForeignKey('entrepreneur.id'))
    entrepreneur = relationship(
        Entrepreneur,
        backref=backref('entrepreneur',
                        uselist=True,
                        cascade='delete-orphan, all'))

    def __str__(self):
        return self.name
