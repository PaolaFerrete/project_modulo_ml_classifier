import os
import pytest
import pandas as pd
from ml_classifier.ml_model import train_classifier, save_model
from sklearn.ensemble import RandomForestClassifier

def test_train_classifier_returns_model(sample_data):
    """Verifica se a função retorna um objeto RandomForest treinado."""
    X = sample_data.drop(columns=['target'])
    y = sample_data['target']
    
    model = train_classifier(X, y, n_estimators=10)
    
    # Verifica se o objeto retornado é do tipo esperado
    assert isinstance(model, RandomForestClassifier)
    # Verifica se o modelo foi 'fitado' (treinado)
    assert hasattr(model, "estimators_")

def test_save_model_creates_file(sample_data, tmp_path):
    """Verifica se o modelo é salvo fisicamente no disco."""
    X = sample_data.drop(columns=['target'])
    y = sample_data['target']
    model = train_classifier(X, y, n_estimators=5)
    
    # tmp_path é uma fixture do pytest que cria uma pasta temporária segura no Ubuntu
    file_path = tmp_path / "model_test.joblib"
    save_model(model, str(file_path))
    
    assert os.path.exists(file_path)