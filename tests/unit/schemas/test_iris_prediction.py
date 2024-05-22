import pytest

from src.schemas.prediction.iris_prediction import IrisPrediction


def test_create_iris_prediction():
    """Test creating an instance of IrisPrediction."""
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2
    species = "setosa"

    iris_prediction = IrisPrediction(
        features={
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        },
        species=species
    )

    assert iris_prediction.features.sepal_length == sepal_length
    assert iris_prediction.features.sepal_width == sepal_width
    assert iris_prediction.features.petal_length == petal_length
    assert iris_prediction.features.petal_width == petal_width
    assert iris_prediction.species == species

def test_invalid_iris_prediction():
    """Test creating an instance of IrisFeatures with invalid values."""
    # You can add test cases here to validate handling of invalid input values
    with pytest.raises(ValueError):
        IrisPrediction(features={"sepal_lenath":"XPTO"}, species="setosa")

    with pytest.raises(ValueError):
        IrisPrediction(features={"sepal_length":5.1, "sepal_width":3.5, "petal_length":1.4})