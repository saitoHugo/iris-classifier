import pickle
import numpy as np

class IrisModelMonostate:
    """
    Monostate class to load the model and species in memory.
    """
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not hasattr(self, 'model'):
            self.model = pickle.load(open('artifacts/prod/RandomForest.pkl', 'rb'))
            self.SPECIES_MAP = {
                0: 'setosa',
                1: 'versicolor',
                2: 'virginica'
            }


    