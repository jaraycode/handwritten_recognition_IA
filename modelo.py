import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds
import sys
from tensorflow.python.keras import layers, models, losses, metrics

def normalize(image, label):
    return tf.cast(image, tf.float32)/255.,label

if __name__ == "__main__":
    # Creando el modelo
    print("Creando modelo...")
    m = models.Sequential(layers=[layers.Flatten(input_shape=(28,28,1)),
                                  layers.Dense(50, activation=tf.nn.relu),
                                  layers.Dense(50, activation=tf.nn.relu),
                                  layers.Dense(27, activation=tf.nn.softmax)])
    
    # no funciona debido a un bug en el lenguaje y el sistema de recursion sys.setrecursionlimit(100000)
    # mnist trabaja con numeros, se necesita usar letras que es el caso de EMNIST
    (ds_train, ds_test), ds_info = tfds.load('mnist', split=['train', 'test'], shuffle_files=True, as_supervised=True, with_info=True)

    # Datos de prueba
    ds_train.map(normalize, num_parallel_calls=tf.data.AUTOTUNE)
    ds_train = ds_train.cache()
    ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
    ds_train = ds_train.batch(128)
    ds_train = ds_train.prefetch(tf.data.AUTOTUNE)

    # Datos de validacion
    ds_test = ds_test.map(normalize, num_parallel_calls=tf.data.AUTOTUNE)
    ds_test = ds_test.cache()
    ds_test = ds_test.batch(128)
    ds_test = ds_test.prefetch(tf.data.AUTOTUNE)

    # Compilar modelo
    m.compile(optimizer='adam', loss=losses.SparseCategoricalCrossentropy(from_logits=True), metrics=[metrics.SparseCategoricalAccuracy()])
    # Entrenar modelo
    historia = m.fit(ds_train, epochs=5, validation_data=ds_test)
    # Mostrar gráfica de pérdida
    plt.xlabel("Epocas")
    plt.ylable("Porcentaje de pérdida")
    plt.plot(historia.history['loss'])
