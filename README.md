# Reconocimiento de letras

Este sistema desarrollado en Python con el uso de las librerías Scikit-learn y TensorFlow es usado para el reconocimiento de letras una vez que sean escritas a mano, retornando las mismas letras en máquina.

## Consideraciones iniciales

- Es necesario el analisis de las entradas, para que puedan quedar las fotos en el formato 28x28 píxeles.
- Creación del modelo siguiendo un patrón de cuantas capas ocultas y cuál función de activación vamos a usar para estos casos (una de las más recomendadas es ReLU).
- Algoritmo que toma todas las imagenes a partir del dataframe del dataset.
- Usar tensorflow.js para poder renderizar html con un cuadro en donde se pueda escribir con el mouse.
- Exportar modelo y guardarlo en su carpeta para que se pueda tener listo en el momento de presentarlo.

### Requisitos

Todos los requisitos quedarán en el archivo requirements.txt
