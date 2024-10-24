import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

class ExploraAnalysis():
    """
    Clase para análisis exploratorio de datos (EDA).
    
    Incluye información general, análisis de nulos, visualizaciones (histogramas, boxplots, scatter matrix),
    detección de outliers, eliminación de duplicados e imputación de valores faltantes usando CatBoost.
    
    Ejecuta automáticamente todo el EDA con la función 'run_full_analysis'.
    """
    
    def __init__(self, data, dataset_name):
        """
        Inicializa la clase con el dataframe de datos y el nombre del dataset.
        """
        self.df = data
        self.dataset_name = dataset_name  # Añadir el nombre del dataset

    def general_information(self):
        """ Muestra información general sobre el dataframe. """
        print("-------------------------------------------")
        print(f"Información General del dataset '{self.dataset_name}':")
        print("-------------------------------------------")
        self.df.info()

    def null_data(self):
        """ Muestra la cantidad de datos nulos en cada columna. """
        print("--------------------------------------------------")
        print(f"Cantidad de datos nulos en el dataset '{self.dataset_name}':")
        print("--------------------------------------------------")
        print(self.df.isnull().sum())

    def random_sample(self):
        """ Muestra una muestra aleatoria de 30 filas del dataframe. """
        print("-----------------------------------------")
        print(f"Muestra Aleatoria del dataset '{self.dataset_name}':")
        print("-----------------------------------------")
        print(self.df.sample(30))

    def descript_statis(self):
        """ Muestra estadísticas descriptivas para columnas numéricas. """
        print("--------------------------------------------------")
        print(f"Estadísticas Descriptivas del dataset '{self.dataset_name}':")
        print("--------------------------------------------------")
        if self.df.select_dtypes(include=['number']).empty:
            print("No hay columnas numéricas para mostrar estadísticas descriptivas.")
        else:
            print(self.df.describe())

    def corre_matri(self):
        """ Calcula y muestra la matriz de correlación para columnas numéricas. """
        print("---------------------------------------------")
        print(f"Matriz de Correlación del dataset '{self.dataset_name}':")
        print("---------------------------------------------")
        if self.df.select_dtypes(include=['number']).empty:
            print("No hay columnas numéricas para mostrar matriz de correlación.")
        else:
            numeric_columns = self.df.select_dtypes(include=['number']).columns
            correlation_matrix = self.df[numeric_columns].corr()
            print(correlation_matrix)

    def basic_histogram(self):
        """ Muestra y guarda histogramas de todas las columnas numéricas. """
        # Asegúrate de que la carpeta exista
        output_dir = 'files/modeling_output/insights/basic_histogram'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for column in numeric_columns:
            plt.figure(figsize=(10, 6))
            
            # Genera el histograma
            plt.hist(self.df[column].dropna(), bins=30, color='skyblue', edgecolor='black')
            plt.title(f'Histograma de {column} en el dataset {self.dataset_name}')
            plt.xlabel(column)
            plt.ylabel('Frecuencia')
            plt.tight_layout()

            # Guardar la figura
            try:
                plt.savefig(f'{output_dir}/histogram_{self.dataset_name}_{column}.png', bbox_inches='tight')
                plt.close()  # Cerrar la figura para evitar problemas de memoria
            except Exception as e:
                print(f"Error al guardar el histograma para {column}: {e}")

            print(f"Histograma de {column} guardado en {output_dir}/histogram_{self.dataset_name}_{column}.png")
            
    def basic_boxplots(self):
        """ Muestra diagramas de caja (boxplots) para todas las columnas numéricas. """
        output_dir = 'files/modeling_output/insights/basic_boxplots'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for column in numeric_columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=self.df, y=column, palette='coolwarm')
            plt.title(f'Boxplot de {column} en el dataset {self.dataset_name}')
            plt.ylabel(column)
            plt.tight_layout()

            # Guardar la figura
            try:
                plt.savefig(f'{output_dir}/boxplot_{self.dataset_name}_{column}.png', bbox_inches='tight')
                plt.close()  # Cerrar la figura para evitar problemas de memoria
                print(f"Boxplot de {column} guardado en {output_dir}/boxplot_{self.dataset_name}_{column}.png")
            except Exception as e:
                print(f"Error al guardar el boxplot para {column}: {e}")
            
    def scatter_matrix_plot(self):
        """ Muestra la matriz de dispersión (scatter matrix) para columnas numéricas. """
        output_dir = 'files/modeling_output/insights/basic_scatter_matrix'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        numeric_columns = self.df.select_dtypes(include=['number']).columns
        if len(numeric_columns) > 1:
            # Usar sns.pairplot para visualizar la matriz de dispersión
            pairplot = sns.pairplot(self.df[numeric_columns], diag_kind='kde')
            pairplot.fig.suptitle(f'Matriz de Dispersión del dataset {self.dataset_name}', y=1.02)  # Ajustar el título

            # Guardar la figura
            try:
                pairplot.savefig(f'{output_dir}/scatter_matrix_{self.dataset_name}.png')
                plt.close()
                print(f"Matriz de dispersión guardada en {output_dir}/scatter_matrix_{self.dataset_name}.png")
            except Exception as e:
                print(f"Error al guardar la matriz de dispersión: {e}")
        else:
            print("No hay suficientes columnas numéricas para crear una matriz de dispersión.")            
            
    def remove_duplicate_rows(self, subset=None, inplace=False):
        
        """
        Elimina filas duplicadas del dataframe.

        Args:
        - subset (list or None): Lista de columnas para considerar al identificar filas duplicadas. Si es None, se consideran todas las columnas.
        - inplace (bool): Si es True, modifica el dataframe actual; si es False, devuelve un nuevo dataframe sin las filas duplicadas.

        Returns:
        - DataFrame or None: DataFrame sin filas duplicadas si inplace es False, None si inplace es True.
        """        
        
        if subset is None:
            subset = self.df.columns.tolist()

        duplicate_rows_before = self.df.duplicated(subset=subset).sum()

        if duplicate_rows_before > 0:
            if inplace:
                self.df.drop_duplicates(subset=subset, inplace=True)
                print(f"Se eliminaron {duplicate_rows_before} filas duplicadas.")
            else:
                result = self.df.drop_duplicates(subset=subset)
                print(f"Se eliminaron {duplicate_rows_before} filas duplicadas.")
                return result
        else:
            print("No se encontraron filas duplicadas.")
            if inplace:
                return None
    
    def run_general_analysis(self):
        """ Ejecuta el análisis general sobre el dataframe. """
        print("-----------------------------------------------------")
        print(f"Iniciando Análisis General del dataset '{self.dataset_name}'...")
        print("-----------------------------------------------------")
        self.general_information()
        self.null_data()
        self.random_sample()
        print("-----------------------------------------------------")
        print(f"Análisis General del dataset '{self.dataset_name}' Completo.")
        print("-----------------------------------------------------")
        

    def descriptive_analysis(self):
        """ Ejecuta análisis de estadísticas descriptivas. """
        print("--------------------------------------------------------------------------")
        print(f"Iniciando Análisis de Estadísticas Descriptivas del dataset '{self.dataset_name}'...")
        print("--------------------------------------------------------------------------")
        self.descript_statis()
        self.corre_matri()
        self.remove_duplicate_rows()
        print("---------------------------------------------------------------------")
        print(f"Análisis de Estadísticas Descriptivas del dataset '{self.dataset_name}' Completo.")
        print("---------------------------------------------------------------------")

    def run_visualization_analysis(self):
        """ Ejecuta análisis de visualización de datos. """
        print("-----------------------------------------------------")
        print(f"Iniciando Análisis de Visualización de Datos del dataset '{self.dataset_name}'...")
        print("-----------------------------------------------------")
        self.basic_histogram()
        self.basic_boxplots()
        self.scatter_matrix_plot()
        print("-----------------------------------------------------")
        print(f"\nAnálisis de Visualización de Datos del dataset '{self.dataset_name}' Completo.")
        print("-----------------------------------------------------")