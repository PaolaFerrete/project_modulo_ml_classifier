from setuptools import setup, find_packages

setup(
    name="machine_learning_classifier",
    version="0.1.0",
    author="Paola Ferrete",
    description="Um pacote para automação de modelos de classificação",
    packages=find_packages(), # Encontra automaticamente as pastas com __init__.py
    install_requires=[
        "pandas",
        "scikit-learn",
        "joblib"
    ],
    python_requires=">=3.8",
)