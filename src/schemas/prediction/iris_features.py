from pydantic import BaseModel

class IrisFeatures(BaseModel):
    """
    Features to predict the iris species."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float