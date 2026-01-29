import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_clean(path):
    """Carrega um CSV e remove linhas com valores nulos."""
    df = pd.read_csv(path)
    return df.dropna()

def split_data(df, target_column, test_size=0.2):
    """Divide o DataFrame em conjuntos de treino e teste."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=42)