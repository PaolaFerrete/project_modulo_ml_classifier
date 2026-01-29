# Machine Learning Classifier Project 🍷

Este projeto foi desenvolvido como parte da atividade modular de Python para IA. Ele consiste em um pacote estruturado para processamento de dados e treinamento de modelos de Machine Learning, utilizando o dataset **Wine** do Scikit-Learn.

## 🚀 Estrutura do Projeto

O projeto segue as melhores práticas de engenharia de software e organização de pacotes Python:

project_modulo_python/
├── ml_classifier/          # Pasta principal do pacote
│   ├── metrics/            # Submódulo para métricas e avaliação
│   ├── ml_model.py         # Lógica de treinamento e persistência
│   └── ml_process.py       # Limpeza e divisão de dados
├── models/                 # Pasta onde os modelos são salvos
├── tests/                  # Testes automatizados (Pytest)
├── notebooks/              # Demonstração e exploração (Jupyter)
├── Makefile                # Automação de tarefas (install, test, clean)
├── requirements.txt        # Dependências do projeto
├── setup.py                # Metadados e instalação do pacote
└── README.md               # Este guia

## 🛠️ Passo-a-passo de Instalação do Projeto

1. Criar e ativar o ambiente virtual

```
python3 -m venv venv
source venv/bin/activate
```
2. Instalar as dependências

```
pip install -r requirements.txt
```

3. Instalar o pacote em modo editável

```
pip install -e .
```

**Também é possível utilizar o Makefile**

- ```make install```
- ``` make test ```
- ``` make clean ```

## 🧪 Rodar os Testes

1. Via **pytest** direto no terminal 

```
pytest -v

```
2. Via **Makefile**

```
make test
```