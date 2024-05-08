import os
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from tf_keras import losses, models, layers, metrics
import tensorflow_datasets as tfds

tfds.load('emnist', ['train', 'test'], shuffle_files=True, as_supervised=True, with_info=True)

DATASET_JONAS = "dataset/archive"

def grafic(modelo):
    plt.xlabel("Épocas")
    plt.ylabel("Pérdida")
    plt.plot(modelo.history["loss"], label="Datos de entrenamiento")
    plt.plot(modelo.history["val_loss"], label="Datos de prueba")
    plt.legend(loc="upper right")
    plt.ylim([0,1])
    plt.show()

def normalize(image):
    return image/255.

def get_word():
    pass

if __name__ == "__main__":
    # Creando el modelo
    print("Creando modelo...")
    m = models.Sequential(layers=[
    layers.Flatten(input_shape=(784,)),
    layers.Dense(125, activation='relu'),
    layers.Dropout(0.03), # Para evitar el overfitting
    layers.Dense(125, activation='relu'),
    layers.Dropout(0.03),
    layers.Dense(125, activation='relu'),
    layers.Dropout(0.03),
    layers.Dense(27, activation='softmax')])

    m.compile(optimizer='adam', loss=losses.SparseCategoricalCrossentropy(from_logits=True), metrics=[metrics.SparseCategoricalAccuracy()])
    
    # Datos de entrenamiento
    df_train = pd.read_csv(os.path.join(DATASET_JONAS, "emnist-letters-train.csv"), header=None)
    df_train = df_train.sample(frac=1)
    df_train_label = df_train.pop(0)
    num_train = df_train.__len__()
    df_train = df_train.map(normalize)

    # Datos de prueba
    df_test = pd.read_csv(os.path.join(DATASET_JONAS, "emnist-letters-test.csv"), header=None)
    df_test = df_test.sample(frac=1)
    df_test_label = df_test.pop(0)
    df_test = df_test.map(normalize)
    df_test

    # Compilar modelo
    m.compile(optimizer='adam', loss=losses.SparseCategoricalCrossentropy(from_logits=True), metrics=[metrics.SparseCategoricalAccuracy()])
    # Entrenar modelo
    historia = m.fit(df_train, df_train_label, epochs=5, validation_data=[df_test, df_test_label])
    # Mostrar gráfica de pérdida
    grafic(historia)
