# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Definir la ruta del archivo CSV que contiene los datos de los juegos
file_path = './Games.csv'

# Leer el archivo CSV en un DataFrame de pandas
games_df = pd.read_csv(file_path)

# Calcular el porcentaje de puntaje multiplicando la puntuación original por 10
games_df['Porcentaje_Puntaje'] = games_df['Score'] * 10

# Seleccionar los 10 mejores juegos del DataFrame
top_10_games = games_df.head(10)

# Crear una figura con un tamaño específico
plt.figure(figsize=(10, 7))

# Crear un gráfico de barras que muestre el porcentaje de puntaje de los 10 juegos seleccionados
barras = plt.bar(top_10_games['GameName'], top_10_games['Porcentaje_Puntaje'], color='#400036')

# Añadir etiquetas a los ejes
plt.xlabel('Juegos')                           # Eje x
plt.ylabel('Valoración en porcentaje (%)')     # Eje y

# Añadir un título al gráfico
plt.title('Top 10 mejores Juegos')

# Rotar las etiquetas del eje x para mejorar la legibilidad
plt.xticks(rotation=45, ha='right')

# Añadir etiquetas de porcentaje en la parte superior de cada barra
for barra in barras:
    yval = barra.get_height()  # Obtener la altura de cada barra
    plt.text(barra.get_x() + barra.get_width()/2, yval + 1, f'{yval:.0f}%', 
             ha='center', va='bottom')  # Colocar el texto en la posición correcta

# Ajustar el diseño del gráfico para que se vea mejor
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Análisis del gráfico:
# El gráfico de barras muestra la valoración en porcentaje de los 10 mejores juegos.
# Cada barra representa un juego, con su respectivo porcentaje de valoración en el eje y.
# Las etiquetas en la parte superior de cada barra indican el porcentaje exacto, lo que permite una
# fácil comprensión de la puntuación de cada juego.
