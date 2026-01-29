import pytest
import pandas as pd

@pytest.fixture
def sample_data():
    """Cria um DataFrame fake para ser usado nos testes."""
    return pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'target': [0, 1, 0, 1, 0]
    })