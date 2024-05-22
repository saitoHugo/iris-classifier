# models/prediction.py
from sqlalchemy import Column, Integer, Float, String
from .database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    sepal_length = Column(Float, index=True)
    sepal_width = Column(Float, index=True)
    petal_length = Column(Float, index=True)
    petal_width = Column(Float, index=True)
    species = Column(String, index=True)