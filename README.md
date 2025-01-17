# Árvores de busca | KNN e SVM | Inteligência Artificial

Este repositório contém implementações de algoritmos de aprendizado de máquina, especificamente voltados para classificação. Abaixo, apresentamos uma visão geral dos scripts disponíveis, suas funcionalidades, casos de uso e exemplos de aplicação.

## Scripts Disponíveis

1. **Arvore1.ipynb**
2. **Arvore2.ipynb**
3. **KNN.ipynb**
4. **SVM.py**

### 1. Arvore1.ipynb

**Funcionalidade:**
Implementa um algoritmo de Árvore de Decisão para tarefas de classificação.

**Casos de Uso:**
- Classificação de dados em categorias distintas com base em atributos predefinidos.
- Identificação de padrões nos dados que podem ser representados hierarquicamente.


### 2. Arvore2.ipynb

**Funcionalidade:**
Fornece uma variação e aprimoramento do algoritmo de Árvore de Decisão apresentado em `Arvore1.ipynb`, tulizando dados extraídos de um dataset `csv`.

**Casos de Uso:**
- Situações onde uma abordagem diferente na construção da árvore pode melhorar a precisão ou interpretabilidade do modelo.
- Comparação de diferentes técnicas de construção de árvores para determinar a mais eficaz para um conjunto de dados específico.


### 3. KNN.ipynb

**Funcionalidade:**
Implementa o algoritmo K-Nearest Neighbors (KNN) para classificação.

**Casos de Uso:**
- Classificação onde a proximidade entre os dados é uma indicação de similaridade.
- Problemas onde a decisão é influenciada pelos exemplos mais próximos no espaço de atributos.

### 4. SVM/SVM.py

**Funcionalidade:**
Implementa o algoritmo de Support Vector Machine (SVM) para classificação.

**Casos de Uso:**
- Classificação binária e multiclasse com margens de decisão bem definidas.
- Problemas onde é importante encontrar o hiperplano que melhor separa as classes.



## Como Utilizar

1. **Pré-requisitos:**
   - Python instalado na máquina.
   - Bibliotecas necessárias: `numpy`, `pandas`, `scikit-learn`, `matplotlib`.

2. **Passos:**
   - Clone este repositório:
     ```bash
     git clone https://github.com/Parreirass/TrabalhoIA.git
     ```
   - Navegue até o diretório do repositório:
     ```bash
     cd TrabalhoIA
     ```
   - Instale as dependências necessárias:
     ```bash
     pip install -r requirements.txt
     ```
   - Abra os notebooks Jupyter:
     ```bash
     jupyter notebook
     ```
   - Execute os notebooks para treinar e avaliar os modelos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias, correções ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

*Observação:* Este README foi gerado com base nas informações disponíveis no repositório e pode ser atualizado conforme o desenvolvimento do projeto.
