# Árvores de busca | KNN e SVM | Inteligência Artificial

Este repositório contém implementações de algoritmos de aprendizado de máquina, especificamente voltados para classificação. Abaixo, apresentamos uma visão geral dos scripts disponíveis, suas funcionalidades, casos de uso e exemplos de aplicação.

## Scripts Disponíveis

1. **Arvore1.ipynb**
2. **Arvore2.ipynb**
3. **KNN.ipynb**
4. **SVM.py**

## 1. Arvore1.ipynb

**Funcionalidade:**
Este código implementa uma **árvore de decisão** simples que fornece sugestões de carreira ou hobbies com base nas preferências do usuário. Ele solicita uma série de respostas a perguntas sobre gostos pessoais e atividades, como trabalhar em equipe, gostar de atividades ao ar livre, preferir trabalhar com tecnologia, entre outras. Com base nas respostas, o código sugere diferentes áreas de atuação profissional ou atividades de lazer.

**Casos de Uso:**
- Classificação de dados em categorias distintas com base em atributos predefinidos.
- Identificação de padrões nos dados que podem ser representados hierarquicamente.

### Como Funciona

O código começa com uma pergunta sobre o gosto do usuário em trabalhar em equipe. A partir da resposta, ele segue uma série de perguntas para definir melhor os interesses e sugestões, passando por questões como comunicação, tecnologia, resolução de problemas, artes, entre outras. Cada resposta leva o usuário por um caminho específico, até chegar a uma recomendação.

### Árvores de Decisão

**Árvores de decisão** são um tipo de modelo preditivo usado em aprendizado de máquina e inteligência artificial. Elas dividem um problema em partes menores com base em perguntas sucessivas, representadas como "nós" na árvore. Cada nó de decisão faz uma pergunta, e as respostas determinam o caminho a seguir até alcançar uma decisão ou recomendação final (representada pelas "folhas" da árvore).

#### Vantagens das Árvores de Decisão:
- Fácil interpretação, já que as decisões podem ser visualizadas como um caminho de perguntas e respostas.
- Podem ser aplicadas tanto para problemas de classificação quanto de regressão.
  
#### Desvantagens:
- Podem ser propensas ao **overfitting** (ajuste excessivo) quando a árvore é muito complexa.
- A precisão pode ser comprometida se a árvore não for bem ajustada.


## 2. Arvore2.ipynb

**Funcionalidade:**
Fornece uma variação e aprimoramento do algoritmo de Árvore de Decisão apresentado em `Arvore1.ipynb`, tulizando dados extraídos de um dataset `csv`.

**Casos de Uso:**
- Situações onde uma abordagem diferente na construção da árvore pode melhorar a precisão ou interpretabilidade do modelo.
- Comparação de diferentes técnicas de construção de árvores para determinar a mais eficaz para um conjunto de dados específico.

### Árvores de Decisão para Análise de Jogadores de Futebol

Este projeto permite filtrar e encontrar jogadores de futebol com base em diferentes critérios, como posição, idade, habilidades e outros atributos. O código utiliza um arquivo CSV contendo informações sobre jogadores e aplica uma abordagem de árvore de decisão para selecionar jogadores que atendem aos requisitos definidos pelo usuário.

### Funcionalidades

#### 1. Filtragem de Jogadores por Posição
O usuário pode selecionar entre diferentes tipos de jogadores: **Defensores**, **Atacantes** e **Meias**.

- **Defensores**: A filtragem inclui opções para tipos de defensores como **GK** (goleiro), **CB** (zagueiro central), **RB** (lateral direito), e **LB** (lateral esquerdo). Dependendo do tipo de defensor escolhido, o código solicita atributos como altura, precisão em cabeceios, salto e força.
- **Atacantes**: O código permite que o usuário defina critérios para jogadores com posições de **ST** (centroavante), **LW** (ponta esquerda) e **RW** (ponta direita). Os critérios incluem habilidades como finalização, controle de bola e precisão em cabeceios.
- **Meias**: O código permite selecionar entre diferentes tipos de meias, como **CM** (meio-campo), **CAM** (meio-campo ofensivo), **CDM** (volante), **RM** (meia direita) e **LM** (meia esquerda). O usuário pode definir critérios como drible, passes longos, visão e reações.

#### 2. Filtragem de Jogadores por Atributos
Além da posição, o código permite que o usuário defina valores mínimos para uma série de atributos dos jogadores, incluindo:

- **Finishing**: Finalização.
- **Dribbling**: Habilidade de drible.
- **Acceleration**: Aceleração.
- **Strength**: Força.
- **Heading Accuracy**: Precisão em cabeceios.
- **Ball Control**: Controle de bola.
- **Reactions**: Reações rápidas.
- **Crossing**: Habilidade de cruzamento.

### 3. Cálculo de Distâncias
O código calcula a "distância" entre os jogadores com base nos critérios fornecidos. Para cada jogador, uma medida de distância é calculada considerando as diferenças absolutas entre os valores dos atributos do jogador e os valores de referência definidos pelo usuário. O código então retorna os 10 jogadores mais próximos com base nessa distância.

### 4. Exibição dos Resultados
Após filtrar os jogadores com base nos critérios definidos, o código exibe uma tabela com os jogadores encontrados, mostrando o nome, idade, posição e classificação geral.

### Exemplo de Execução

```bash
Qual posição geral deseja (Defensor, Atacante, Meia)? Defensor
Qual tipo de defensor (GK, CB, RB, LB)? CB
Qual é a altura mínima em cm? 180
Qual é o valor mínimo para heading_accuracy? 70
Qual é o valor mínimo para jumping? 75
Qual é o valor mínimo para strength? 80
Qual é a faixa etária do jogador? 25
Qual é a classificação geral mínima (overall_rating)? 80
+------------------+-----+------------+------------------+
| name             | age | positions  | overall_rating   |
+------------------+-----+------------+------------------+
| João Silva       | 24  | CB         | 85               |
| Lucas Oliveira   | 26  | CB         | 82               |
| Bruno Costa      | 23  | CB         | 80               |
+------------------+-----+------------+------------------+
```

## 3. KNN.ipynb

**Funcionalidade:**
Implementa o algoritmo K-Nearest Neighbors (KNN) para classificação.

**Casos de Uso:**
- Classificação onde a proximidade entre os dados é uma indicação de similaridade.
- Problemas onde a decisão é influenciada pelos exemplos mais próximos no espaço de atributos.

### Classificação de Qualidade de Vinhos com K-Nearest Neighbors (KNN)

Este projeto utiliza a classificação de vinhos com base em suas propriedades químicas para prever a qualidade do vinho. O modelo de aprendizado de máquina K-Nearest Neighbors (KNN) é utilizado para classificar os vinhos. O código foi desenvolvido utilizando as bibliotecas `pandas`, `scikit-learn`, `matplotlib`, `seaborn` e `tabulate` para análise de dados, visualização e modelagem.

#### Funcionalidades

- Carrega e prepara um dataset de vinhos.
- Realiza a análise e visualização dos dados.
- Preprocessa os dados para treinamento e teste do modelo.
- Aplica o algoritmo de K-Nearest Neighbors (KNN) para classificação.
- Avalia o modelo utilizando métricas de acurácia e outras avaliações.
- Gera gráficos para análise exploratória dos dados.

### Sobre o K-Nearest Neighbors (KNN)

O K-Nearest Neighbors (KNN) é um algoritmo de aprendizado supervisionado utilizado para tarefas de classificação e regressão. No contexto deste projeto, o KNN é usado para **classificar a qualidade do vinho** com base em suas características químicas. 

O algoritmo funciona da seguinte maneira:

1. **Escolha de K**: O usuário escolhe um valor de K, que representa o número de vizinhos mais próximos a serem considerados para determinar a classe de uma amostra.
2. **Cálculo de Distâncias**: Para uma nova amostra, o KNN calcula a distância entre essa amostra e todas as outras no conjunto de treinamento, geralmente utilizando métricas como a distância Euclidiana.
3. **Votação**: A classe da amostra é determinada pela classe majoritária entre os K vizinhos mais próximos.
4. **Predição**: O modelo faz uma predição para a amostra com base nas classes dos seus vizinhos.

#### Vantagens:
- Simples de implementar e entender.
- Não faz suposições sobre a distribuição dos dados (não é paramétrico).
- Funciona bem com conjuntos de dados pequenos e com boa separação entre as classes.

#### Desvantagens:
- Pode ser computacionalmente caro para grandes datasets, pois exige o cálculo das distâncias para todas as amostras no conjunto de dados.
- A escolha do valor de K é importante: valores muito pequenos podem causar overfitting, enquanto valores muito grandes podem suavizar demais as decisões.

Neste projeto, foi utilizado um valor de K igual a 15, o que significa que o algoritmo considera os 15 vizinhos mais próximos para classificar a qualidade do vinho.



## 4. SVM/SVM.py

**Funcionalidade:**
Implementa o algoritmo de Support Vector Machine (SVM) para classificação de qualidade vinhos.

**Casos de Uso:**
- Classificação binária e multiclasse com margens de decisão bem definidas.
- Problemas onde é importante encontrar o hiperplano que melhor separa as classes.

### Análise de Qualidade do Vinho com PCA e SVM

#### Descrição do Projeto

Este projeto utiliza a combinação de **PCA (Principal Component Analysis)** e **SVM (Support Vector Machine)** para classificar a qualidade do vinho com base em suas características químicas. O modelo é treinado e avaliado em um conjunto de dados que contém atributos como acidez, álcool, pH, entre outros.

#### Objetivos

- **Redução de Dimensionalidade**: Utilizamos o PCA para reduzir a quantidade de atributos do conjunto de dados e focar nas características mais relevantes para a classificação.
- **Classificação**: Utilizamos o SVM para classificar a qualidade do vinho com base nos dados reduzidos.

#### Passos do Código

1. **Carregamento do Conjunto de Dados**: O arquivo CSV com as informações sobre o vinho é carregado usando o pandas.
2. **Pré-processamento**: O conjunto de dados é dividido em características (X) e a variável alvo (y). Em seguida, os dados são normalizados utilizando o `StandardScaler`.
3. **Redução de Dimensionalidade com PCA**: O PCA é aplicado para reduzir a dimensionalidade dos dados a 10 componentes principais.
4. **Treinamento do Modelo SVM**: O modelo SVM é treinado utilizando o conjunto de dados reduzido.
5. **Avaliação do Modelo**: O modelo SVM é avaliado utilizando a precisão (accuracy) no conjunto de teste.

### Sobre o SVM (Support Vector Machine)

O **SVM (Support Vector Machine)** é um algoritmo de aprendizado supervisionado utilizado principalmente para tarefas de **classificação** e, em menor grau, para **regressão**. Ele encontra um **hiperplano** que separa os dados de diferentes classes com a maior margem possível, o que ajuda a melhorar a precisão e reduzir o erro de classificação.

#### Funcionamento:

- **Separação Linear**: Para dados que são linearmente separáveis, o SVM encontra um hiperplano que divide as classes de forma a maximizar a margem, ou seja, a distância entre o hiperplano e os pontos mais próximos de cada classe (chamados de **vetores de suporte**).
  
- **Função Kernel**: Quando os dados não são linearmente separáveis, o SVM utiliza uma função **kernel** para transformar os dados em um espaço de dimensão superior, onde a separação linear é possível. Exemplos de kernels incluem o kernel **linear**, **polinomial** e **RBF (Radial Basis Function)**.
  
- **Margem Máxima**: O objetivo do SVM é encontrar o hiperplano que tem a maior margem entre as classes. A margem é definida pela distância entre o hiperplano e os vetores de suporte.

#### Vantagens:
- Eficaz em **espaços de alta dimensionalidade**.
- Funciona bem para conjuntos de dados com muitas características.
- **Robustez**, especialmente quando se usa o kernel apropriado.

#### Desvantagens:
- Desempenho pode ser mais **lento** para grandes conjuntos de dados.
- A escolha do **kernel** e dos parâmetros (como **C** e **gamma**) pode ser crucial e requer **ajuste**.


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


