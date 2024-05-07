import cv2
import pandas as pd
import numpy as np
from tf_keras import models

# Lista de las letras que se necesitan
LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class Predict():

    def __init__(self) -> None:
        self.modelo = models.load_model("../trainedModel/handwritting.h5")

    def predict(self):
        pass

    def normalize(self, image):
        return float(image/255.)

    def image(self, image):
        imagen = cv2.imread(image)[:,:,0]
        #imagen = np.invert(np.array([imagen]))
        imagen = np.invert(imagen)
        imagen = cv2.resize(imagen, (28,28))
        #imagen = imagen.transpose()
        #img = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        imagen = imagen.flatten()
        df_img = pd.DataFrame(imagen)
        df_img = df_img.map(self.normalize)
        df_img = df_img.T
        #df_img = df_img.to_numpy().flatten()

        #df_img = pd.DataFrame(df_img)
        #df_img = pd.pivot_table(df_img).reset_index()

        #mascara,_ = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
        prediccion = self.modelo.predict(imagen)
        print(f"La predicción indica que su letra es: {LETTERS[np.argmax(prediccion)-1]}")
        #print(df_img)

if __name__ == "__main__":
    prueba = Predict()
    prueba.image("word.jpg")