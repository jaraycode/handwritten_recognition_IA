import tensorflow as tf
import tensorflow.python.keras as tfks
from tensorflow.python.keras import layers, Input
class modelo:
    """
        Modelo de IA con tensorflow, en principio se le están dando las siguientes características
        > Formato de input 28x28 y 1 en tipo de datos
        > 2 Capa oculta con 50 neuronas y función de activación ReLU
        > Capa de salida que permite 27 tipos diferentes de salida debido a que esas son todas las letras disponibles.
    """
    def __init__(self) -> None:
        pass