from pydantic import BaseModel

from .iris_features import IrisFeatures

class IrisPrediction(BaseModel):
    """
    Iris prediction response and used features"""
    features: IrisFeatures
    species: str