from sqlalchemy import Column, DECIMAL, Integer
from sqlalchemy.dialects.postgresql import JSONB

from app.sql_app.database import Base

class Scores(Base):
    """
    """
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True, nullable=False)
    input_requests = Column(JSONB, nullable=False)
    output_response = Column(JSONB, nullable=False)
    score = Column(DECIMAL, nullable=False)
