from sklearn.metrics import accuracy_score, classification_report

def get_accuracy(model, X_test, y_test):
    """Calcula a acurácia do modelo."""
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

def evaluate_model(model, X_test, y_test):
    """Retorna a acurácia e o relatório de classificação."""
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    return acc, report