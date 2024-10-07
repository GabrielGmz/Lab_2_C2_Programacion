# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Definir la ruta del archivo CSV que contiene los datos de los dramas
file_path = './top100_kdrama.csv'

# Leer el archivo CSV en un DataFrame de pandas
kdrama_df = pd.read_csv(file_path)

# Seleccionar los 20 mejores dramas del DataFrame
top_20_kdramas = kdrama_df.head(20)

# Crear una figura con un tamaño específico
plt.figure(figsize=(10, 6))

# Crear un gráfico de líneas que muestre la popularidad de los 20 dramas seleccionados
plt.plot(top_20_kdramas['Title'], top_20_kdramas['Popularity'], 
         marker='o', color='#105057')

# Añadir etiquetas a los ejes
plt.xlabel('Dramas')         # Eje x
plt.ylabel('Puntuación')     # Eje y

# Añadir un título al gráfico
plt.title('Top 20 Mejores Dramas - Puntuación')

# Rotar las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45, ha='right')

# Ajustar el diseño del gráfico para que se vea mejor
plt.tight_layout()

# Añadir una cuadrícula al gráfico para facilitar la lectura de datos
plt.grid(True)

# Mostrar el gráfico
plt.show()

# Análisis del gráfico:
# El gráfico de líneas muestra la relación entre el título de los dramas y su puntuación de popularidad.
# Cada punto en la línea representa un drama, con su respectiva puntuación, y los marcadores ayudan a
# destacar cada drama en la visualización. 


