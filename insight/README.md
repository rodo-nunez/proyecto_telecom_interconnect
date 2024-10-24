# Exploratory EDA

En esta sección realizaremos un análisis exploratorio de datos (EDA) para extraer información clave de nuestros datasets: contract, internet, personal, y phone.

## Tabla de contenidos
1. **Análisis de resultados por dataset**

    1.1 **Análisis contract.csv**: Este dataset contiene información sobre los contratos de los clientes. Después de revisar los datos, no se encontraron valores nulos ni duplicados. El dataset tiene un total de 7043 registros y 8 columnas.

    En cuanto a los cargos mensuales (MonthlyCharges), observamos que la distribución no es normal, ya que la desviación estándar es bastante alta en comparación con la media. Podría ser relevante analizar cómo las características del contrato influyen en la tasa de cancelación.

    *Análisis del histograma*:
    La distribución de los cargos mensuales no es simétrica, presentando una forma multimodal con picos en diferentes rangos. Hay un pico extremadamente alto en el intervalo de $20, lo que sugiere que una gran cantidad de clientes pagan tarifas bajas, probablemente asociadas a planes básicos o con descuentos significativos.

    Entre $40 y $100, la distribución es más homogénea, reflejando una mayor variabilidad en los planes. Sin embargo, hay picos adicionales alrededor de $60, $80 y $100, lo que indica que algunos clientes pagan tarifas más elevadas, probablemente por servicios premium o paquetes adicionales.

    Aunque los valores superiores a $100 tienen menor frecuencia, un pequeño grupo de clientes paga cargos cercanos a los $120, lo que podría representar tarifas especiales o clientes con servicios avanzados.

    Este comportamiento es interesante para analizar la tasa de cancelación. Por ejemplo, los clientes con cargos bajos (alrededor de $20) podrían tener menos incentivos para cancelar, mientras que aquellos con cargos más altos podrían estar en mayor riesgo si perciben que no obtienen el valor esperado por lo que pagan.

    *Análisis del Boxplot*:
    En el boxplot de los cargos mensuales, se observa que el 50% de los clientes se concentra en el rango de $38 a $90, con una media cercana a $70. Los valores extremos tienden a estar más dispersos en la parte superior, lo que refuerza la idea de que algunos clientes pagan tarifas significativamente más altas.

    1.2 Análisis intenrnet.csv: Este dataset contine información sobre los servicios de internet, no se encontro datos nulos y tampoco duplicados. 
    
    1.3 Análisis personal.csv
    
    1.4 Análisis phone.csv