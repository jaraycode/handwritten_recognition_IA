from app.modelo_actions import modelo_actions
import tensorflow as tf
import tensorflow.python.keras as tfks
from tensorflow.python.keras import layers

class modelo_implementation(modelo_actions):

    def __init__(self, modelo) -> None:
        self.modelo = modelo

    def imageToCorrectSize(image, label):
        return tf.cast(image, tf.float32) / 255., label