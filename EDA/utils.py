import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class processing_data:
    def __init__(self,data):
        self.data = data
    def nulls_percent(self):
        """This funtion generated nulls percentage for dataset:
        args:
            self.data: Pandas dataframe 
        return:
            missing_value_df: dataframe with nulls percentage information
        """
        percent_missing = self.data.isnull().sum() * 100 / len(self.data)
        missing_value_df = pd.DataFrame({'column_name': self.data.columns,
                                        'percent_missing': percent_missing})
        missing_value_df.sort_values('percent_missing', inplace=True, ascending=False)
        return missing_value_df
    
class plots_eda:
    def __init__(self,data):
        self.data = data
    def plots_categorical_bars(self):
        """Plot frecuency for all categorical columns in dataframe
        args:
            self.data: Pandas dataframe 
        return:
            sdtout graphic matplot
        """
        self.data = self.data.fillna('NaN')
        # Obtener las columnas categóricas del DataFrame
        columnas_categoricas = self.data.select_dtypes(include=['object'])

        # Crear un diccionario para almacenar los conteos de las categorías
        conteo_categorias = {}

        # Calcular el número de filas para cada categoría en cada columna
        for columna in columnas_categoricas.columns:
            conteo = self.data[columna].value_counts()
            conteo_categorias[columna] = conteo

        # Seleccionar las 20 características más comunes
        caracteristicas_comunes = {}
        for columna, conteo in conteo_categorias.items():
            caracteristicas_comunes[columna] = list(conteo.head(5).index)

        # Crear subgráficos para las características más comunes
        fig, axes = plt.subplots(nrows=len(columnas_categoricas.columns), figsize=(6, 4*len(columnas_categoricas.columns)))
        
        # Recorrer las columnas categóricas y crear los gráficos de barras para las características más comunes
        for i, (columna, caracteristicas) in enumerate(caracteristicas_comunes.items()):
            ax = axes[i]
            self.data[columna].value_counts().loc[caracteristicas].plot(kind='bar', ax=ax)
            ax.set_title(f'Conteo de filas por categoría en {columna}')
            ax.set_xlabel('Categoría')
            ax.set_ylabel('Número de filas')

        # Ajustar el espaciado entre los subgráficos
        plt.tight_layout()

        # Mostrar el gráfico
        plt.show()

