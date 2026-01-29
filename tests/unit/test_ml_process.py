import pandas as pd
import pytest
from ml_classifier.ml_process import split_data

def test_split_data_shapes():
    """ Testa se os dados são divididos corretamente em treino e teste"""
    df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [0, 1, 0, 1, 0]})
    X_train, X_test, y_train, y_test = split_data(df, 'target')
    assert len(X_train) == 4
    assert len(X_test) == 1

def test_split_data_proportions():
    """ Criando um dataset fake para teste"""
    data = {'feature1': range(10), 'target': [0, 1] * 5}
    df = pd.DataFrame(data)
    
    X_train, X_test, y_train, y_test = split_data(df, 'target', test_size=0.2)
    
    assert len(X_test) == 2
    assert len(X_train) == 8