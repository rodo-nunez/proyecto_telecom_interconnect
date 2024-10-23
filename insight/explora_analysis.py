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

    def interactive_histogram(self):
        """ Muestra histogramas interactivos de todas las columnas numéricas. """
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for column in numeric_columns:
            fig = px.histogram(self.df, x=column, nbins=30, title=f'Histograma de {column} en el dataset {self.dataset_name}')
            fig.show()

    def interactive_boxplots(self):
        """ Muestra diagramas de caja interactivos (boxplots) para todas las columnas numéricas. """
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for column in numeric_columns:
            fig = px.box(self.df, y=column, title=f'Boxplot de {column} en el dataset {self.dataset_name}')
            fig.show()

    def interactive_scatter_matrix(self):
        """ Muestra una matriz de dispersión interactiva (scatter matrix) para todas las columnas numéricas. """
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        fig = px.scatter_matrix(self.df, dimensions=numeric_columns)
        fig.update_traces(diagonal_visible=False)
        fig.show()

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
        print("---------------------------------------------------------------------")
        print(f"Análisis de Estadísticas Descriptivas del dataset '{self.dataset_name}' Completo.")
        print("---------------------------------------------------------------------")

    def run_visualization_analysis(self):
        """ Ejecuta análisis de visualización de datos. """
        print("-----------------------------------------------------")
        print(f"Iniciando Análisis de Visualización de Datos del dataset '{self.dataset_name}'...")
        print("-----------------------------------------------------")
        self.interactive_histogram()
        self.interactive_boxplots()
        self.interactive_scatter_matrix()
        print("-----------------------------------------------------")
        print(f"\nAnálisis de Visualización de Datos del dataset '{self.dataset_name}' Completo.")
        print("-----------------------------------------------------")
        


