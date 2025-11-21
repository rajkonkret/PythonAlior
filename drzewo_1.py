import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
# pip install -U scikit-learn
# Tworzenie przykładowych danych
data = {
    'Pogoda_sloneczna': [1, 1, 0, 0, 1, 0, 1],
    'Temperatura_wysoka': [1, 0, 1, 0, 1, 0, 0],
    'Idziemy_na_spacer': [1, 1, 0, 0, 1, 0, 0]
}
df = pd.DataFrame(data)
X = df[['Pogoda_sloneczna', 'Temperatura_wysoka']]
y = df['Idziemy_na_spacer']

# Budowa modelu
model_drzewa = DecisionTreeClassifier(max_depth=2, random_state=42)
model_drzewa.fit(X, y)

# Wizualizacja drzewa
plt.figure(figsize=(12, 8))
plot_tree(
    model_drzewa,
    feature_names=X.columns,
    class_names=['Zostajemy', 'Idziemy'],
    filled=True,
    rounded=True
)
plt.title("Wizualizacja Drzewa Decyzyjnego")
plt.show()

