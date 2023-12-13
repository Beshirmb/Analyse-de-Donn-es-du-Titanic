
# Import des bibliothèques nécessaires pour les tests
import pandas as pd
from gestion_des_valeur import train  # Assurez-vous d'ajuster le nom du module

def test_train_model():
    # Créez un DataFrame de test
    data = {'Pclass': [1, 2, 3, 1, 2], 'Sex': ['male', 'female', 'male', 'female', 'male'], 'Survived': [1, 0, 1, 0, 1]}
    df = pd.DataFrame(data)

    # Appliquez la fonction d'entraînement du modèle
    model = train.train_model(df)

    # Vérifiez que le modèle est correctement entraîné
    assert model is not None
