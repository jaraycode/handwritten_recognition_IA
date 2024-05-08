import cv2
import pandas as pd
import numpy as np
import tensorflow as tf
from tf_keras import models

# Lista de las letras que se necesitan
LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
np.set_printoptions(precision=3, suppress=True)

class Predict():

    def __init__(self) -> None:
        self.modelo = models.load_model("../trainedModel/handwritting.h5")

    def normalize(self, image):
        return image/255.

    def image(self, image):
        imagen_org = cv2.imread(image)[:,:,0]
        mascara,imagen2 = cv2.threshold(imagen_org,127,255,0)
        contorno, idd = cv2.findContours(imagen2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        contorno_index = sorted(enumerate(contorno), key=lambda x: cv2.boundingRect(x[1][0]))
        #imagen = np.invert(np.array([imagen]))
        
        word = ""

        for origin, contorno2 in contorno_index:
            x,y,z,w = cv2.boundingRect(contorno2)
            if idd[0][origin][3] != -1 and z > 10 and w > 40:
                imagen_for=imagen_org[y:y+w, x:x+z]
                imagen_for=cv2.bitwise_not(imagen_for)                                            
                imagen_for = cv2.resize(imagen_for, (28,28), interpolation=cv2.INTER_AREA)
                # Crear una imagen en blanco para dibujar el contorno
                contour_image = np.zeros_like(imagen_for)
                
                # Dibujar el contorno en la imagen en blanco
                cv2.drawContours(contour_image, [contorno2], -1, (255), thickness=cv2.FILLED)

                #contorno_img = np.zeros_like(imagen)
                imagen_for[contour_image == 255] = 255

                # Determinar si se necesita aplicar espejo horizontal
                #if x < imagen_org.shape[1]:
                #    imagen_for = cv2.flip(imagen_for, 1)  # Espejo horizontal

                # Rotar la imagen 90 grados hacia la izquierda
                #imagen_for = cv2.rotate(imagen_for, cv2.ROTATE_90_COUNTERCLOCKWISE)

                #cv2.imshow("Prueba", imagen_for)
                #cv2.waitKey(0)
        #imagen = imagen.transpose()
        #img = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
                #i = tf.image.resize(imagen_for,(1,784))
                imagen = imagen_for.flatten("F")
                df_img = pd.DataFrame(imagen)
                df_img = df_img.map(self.normalize)
                df_img = df_img.T
                #print(df_img)
                tensor = tf.constant(df_img.to_numpy(np.float32),tf.float32,shape=[1,784])
                prediccion = self.modelo.predict(tensor)
        #tensor = tf.Tensor(df_img.to_numpy(), shape=(784,))
        #tensor = tf.shape(tensor)
        #df_img = df_img.to_numpy().flatten()

        #df_img = pd.DataFrame(df_img)
        #df_img = pd.pivot_table(df_img).reset_index()

        
        #print(tf.shape(tensor))
                word += LETTERS[np.argmax(prediccion)-1]
        print(f"La predicción indica que su letra es: {word}")
        return word

if __name__ == "__main__":
    prueba = Predict()
    prueba.image("word.jpg")