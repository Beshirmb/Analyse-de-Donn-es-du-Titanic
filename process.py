# Import des bibliothèques nécessaires pour les tests
import pandas as pd
from gestion_des_valeurs import process  

def test_handle_missing_values():
    # Créez un DataFrame de test
    data = {'Age': [25, None, 30, 35], 'Embarked': ['S', 'C', 'Q', None]}
    df = pd.DataFrame(data)

    # Appliquez la fonction de gestion des valeurs manquantes
    processed_df = process.handle_missing_values(df)

    # Vérifiez que les valeurs manquantes ont été correctement traitées
    assert not processed_df['Age'].isnull().any()
    assert not processed_df['Embarked'].isnull().any()

