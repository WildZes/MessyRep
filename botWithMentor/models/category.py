from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from models.business import Business

# инициализация декларативного стиля
Base = declarative_base()


class Category(Base):

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    business_id = Column(Integer, ForeignKey('business.id'))
    business = relationship(
        Business,
        backref=backref('business',
                        uselist=True,
                        cascade='delete-orphan, all'))

    def __str__(self):
        return self.name
