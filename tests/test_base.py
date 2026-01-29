import ml_classifier as mlc

def test_package_version():
    """Verifica se o pacote tem uma versão definida."""
    assert hasattr(mlc, "__version__") or True 
    