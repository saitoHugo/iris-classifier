from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from schemas.prediction import IrisFeatures, IrisPrediction
import pandas as pd
router = APIRouter()


from logger import logger

def input_preprocessing(inputs: List[float]) -> pd.DataFrame:
    column_names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
    df = pd.DataFrame([inputs], columns=column_names)
    return df


@router.post("/predict", response_model=IrisPrediction)
def predict_iris(features: IrisFeatures, request: Request):
    """
    Predict the iris species with the given features.

    Args:
        features(IrisFeatures): Features to predict the iris species.
        request(Request): Request object.
    Returns: 
        IrisPrediction: Predicted iris species and used features
    """
    logger.info(f"Predicting iris species with features: {features}")
    #try:
    data = input_preprocessing([features.sepal_length, features.sepal_width, features.petal_length, features.petal_width])
    model = request.app.state.model
    species_map = request.app.state.species_map
    prediction = model.predict(data)
    species = species_map[prediction[0]]
    return IrisPrediction(features=features, species=species)
    # except Exception as e:
    #     logger.error(f"Error predicting iris species: {str(e)}")
    #     raise HTTPException(status_code=400, detail=str(e))

