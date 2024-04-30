from flask import Flask, render_template, request
import cv2
app = Flask(__name__)

LETTERS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def preview(image):
    
    # Asegurar escala de grises
    imagen = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Transformar a forma binaria
    imagen = cv2.threshold(imagen,400,600,cv2.THRESH_BINARY)

    pass

@app.route('/')
@app.route('/<imageName>', methods=['GET','POST'])
def home(imageName=None):
    if request.method == 'POST':
        print(request.form['save_data'])
    return render_template('index.html', prediction_text="inicio")

@app.get('/prediction')
def prediction():
    return {"message": "hola"}

if __name__ == "__main__":
    app.run("0.0.0.0","8000", debug=True)