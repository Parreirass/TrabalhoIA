import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Carregar o arquivo CSV
caminho_do_csv = '../KNN/winequality-red.csv'

# Lê o arquivo CSV e armazena em um DataFrame
data = pd.read_csv(caminho_do_csv)

# Supondo que a última coluna seja a variável alvo (y)
X = data.iloc[:, :-1].values  # Todas as colunas, exceto a última
y = data.iloc[:, -1].values   # A última coluna

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Padronizar os dados (muito importante para PCA e SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Aplicar PCA para reduzir a dimensionalidade
pca = PCA(n_components=10)  # Reduzindo para 2 componentes principais
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Treinar o modelo SVM
svm = SVC(kernel='linear')  # Você pode escolher outros kernels como 'rbf'
svm.fit(X_train_pca, y_train)

# Fazer previsões no conjunto de teste
y_pred = svm.predict(X_test_pca)

# Avaliar a precisão do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')
