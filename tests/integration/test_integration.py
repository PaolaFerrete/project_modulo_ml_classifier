import pandas as pd
from ml_classifier.ml_process import split_data
from ml_classifier.ml_model import train_classifier
from ml_classifier.metrics.ml_accuracy import get_accuracy

def test_full_pipeline():
    # Simulação de pipeline completo
    data = {'feat1': [1,2,3,4,5]*10, 'target': [0,1,0,1,0]*10}
    df = pd.DataFrame(data)
    
    X_train, X_test, y_train, y_test = split_data(df, 'target')
    model = train_classifier(X_train, y_train)
    acc = get_accuracy(model, X_test, y_test)
    
    assert 0 <= acc <= 1