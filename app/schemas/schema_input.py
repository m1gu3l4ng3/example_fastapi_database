from pydantic import BaseModel

class InputRequest(BaseModel):
    """
    """
    score_math: float
    score_science: float
    score_chemistry: float