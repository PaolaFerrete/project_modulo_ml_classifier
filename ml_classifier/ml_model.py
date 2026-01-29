from sklearn.ensemble import RandomForestClassifier
import joblib

def train_classifier(X_train, y_train, n_estimators=100):
    """Treina um modelo Random Forest."""
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(X_train, y_train)
    return model

def save_model(model, filename):
    """Salva o modelo treinado em um arquivo .joblib."""
    path = "../models/" + filename  # Diretório para salvar os modelos
    joblib.dump(model, path)