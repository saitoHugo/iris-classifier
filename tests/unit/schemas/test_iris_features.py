import pytest

from src.schemas.prediction.iris_features import IrisFeatures

def test_create_iris_features():
    """Test creating an instance of IrisFeatures."""
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2

    iris_features = IrisFeatures(
        sepal_length=sepal_length,
        sepal_width=sepal_width,
        petal_length=petal_length,
        petal_width=petal_width
    )

    assert iris_features.sepal_length == sepal_length
    assert iris_features.sepal_width == sepal_width
    assert iris_features.petal_length == petal_length
    assert iris_features.petal_width == petal_width

def test_invalid_iris_features():
    """Test creating an instance of IrisFeatures with invalid values."""
    # You can add test cases here to validate handling of invalid input values
    with pytest.raises(ValueError):
        IrisFeatures(sepal_length="invalid", sepal_width=3.5, petal_length=1.4, petal_width=0.2)

    with pytest.raises(ValueError):
        IrisFeatures(sepal_length=5.1, sepal_width=3.5, petal_length=1.4)