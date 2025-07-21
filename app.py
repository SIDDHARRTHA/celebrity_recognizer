from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('celebrity_face_model.h5')  # Load your trained model

# Class labels mapping (make sure this matches your training)
class_indices = {
    'Angelina Jolie': 0, 'Brad Pitt': 1, 'Denzel Washington': 2, 'Hugh Jackman': 3,
    'Jennifer Lawrence': 4, 'Johnny Depp': 5, 'Kate Winslet': 6, 'Leonardo DiCaprio': 7,
    'Megan Fox': 8, 'Natalie Portman': 9, 'Nicole Kidman': 10, 'Robert Downey Jr': 11,
    'Sandra Bullock': 12, 'Scarlett Johansson': 13, 'Tom Cruise': 14, 'Tom Hanks': 15,
    'Will Smith': 16
}
idx_to_label = {v: k for k, v in class_indices.items()}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    # Save the uploaded file
    filepath = os.path.join('static', file.filename)
    file.save(filepath)

    # Process image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    confidence = np.max(predictions[0]) * 100

    predicted_label = idx_to_label[predicted_index]

    return render_template('result.html', 
                           label=predicted_label, 
                           confidence=f"{confidence:.2f}%", 
                           image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
