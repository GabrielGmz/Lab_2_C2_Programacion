# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Definir la ruta del archivo CSV que contiene los datos de anime
file_path = './Anime_ratings.csv'

# Leer el archivo CSV en un DataFrame de pandas
anime_df = pd.read_csv(file_path)

# Seleccionar los 5 animes más populares del DataFrame
top_5_animes = anime_df.head(5)

# Crear una figura con un tamaño específico
plt.figure(figsize=(8, 10))

# Crear un gráfico circular (de pastel)
plt.pie(top_5_animes['Popularity'], 
        labels=top_5_animes['Title'], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])

# Añadir un título al gráfico
plt.title('Porcentaje de Popularidad en Animes')

# Asegurar que el gráfico de pastel sea circular
plt.axis('equal') 

# Ajustar el diseño del gráfico para que se vea mejor
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Análisis del gráfico:
# El gráfico circular muestra la distribución de la popularidad entre los 5 animes más populares.
# Cada segmento del gráfico representa un anime, con su respectivo porcentaje de popularidad.
# Los colores diferentes ayudan a distinguir entre los animes.

