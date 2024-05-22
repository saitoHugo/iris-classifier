import pytest
from src.models.models_monostate import IrisModelMonostate  

@pytest.fixture
def iris_model():
    """Create an instance of IrisModelMonostate for testing."""
    return IrisModelMonostate()

def test_model_loaded(iris_model):
    """Test that the model is loaded successfully."""
    assert hasattr(iris_model, 'model')

def test_species_map_initialized(iris_model):
    """Test that the species map is correctly initialized."""
    assert hasattr(iris_model, 'SPECIES_MAP')
    assert isinstance(iris_model.SPECIES_MAP, dict)
    assert len(iris_model.SPECIES_MAP) == 3 # 3 species in the Iris dataset
