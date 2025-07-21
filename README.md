# ⭐ Celebrity Face Recognition

A deep learning-powered web application that identifies celebrities from uploaded images using a trained Convolutional Neural Network (CNN). Built using Flask, TensorFlow/Keras, and OpenCV, this project demonstrates real-time face recognition and classification with high accuracy.

## 📸 Demo
Upload an image and get the predicted celebrity name along with confidence level.

**Example:**
- Input: A photo of Leonardo DiCaprio
- Output: Predicted Class: Leonardo DiCaprio (Confidence: 96.5%)

## 🚀 Features
- Upload any celebrity image for recognition
- Real-time predictions with probability confidence
- Clean, responsive UI with centered result display
- About page showcasing the tech stack and model overview
- Model trained on 17 famous celebrities

## 🧠 Model Information
- **Type:** Convolutional Neural Network (CNN)
- **Framework:** TensorFlow & Keras
- **Dataset:** Custom dataset with 17 celebrity classes
- **Classes:**
  - Angelina Jolie, Brad Pitt, Denzel Washington, Hugh Jackman, Jennifer Lawrence, Johnny Depp, Kate Winslet, Leonardo DiCaprio, Megan Fox, Natalie Portman, Nicole Kidman, Robert Downey Jr, Sandra Bullock, Scarlett Johansson, Tom Cruise, Tom Hanks, Will Smith.

## 🛠️ Tech Stack
| Layer        | Technology                |
|--------------|---------------------------|
| Frontend     | HTML, CSS, Bootstrap      |
| Backend      | Flask (Python Web Framework) |
| Model        | Keras (TensorFlow Backend) |
| Preprocessing| OpenCV, NumPy             |

## 📂 Project Structure
```
celebrity-face-recognition/
│
├── static/                # CSS, Images
├── templates/             # HTML templates (index.html, about.html, result.html)
├── model/celebrity_model.h5   # Trained CNN model
├── app.py                 # Flask application
├── requirements.txt       # Project dependencies
├── screenshots/           # App screenshots
└── README.md              # Project overview
```

## 📷 Screenshots
Below are actual screenshots from the app:

![Demo Screenshot 1](screenshots/Screenshot%202025-07-22%20021718.png)
![Demo Screenshot 2](screenshots/Screenshot%202025-07-22%20021742.png)
## ⚙️ Setup Instructions
1. Clone the repo
   ```bash
   git clone https://github.com/your-username/celebrity-face-recognition.git
   cd celebrity-face-recognition
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app
   ```bash
   python app.py
   ```
4. Open in browser
   ```
   http://127.0.0.1:5000/
   ```

## 📈 Future Enhancements
- Add webcam-based face capture
- Expand dataset to include more celebrities
- Add face bounding box and overlay on image
- Deploy online via Render, Railway, or Hugging Face Spaces

## 🧑‍💻 Author
**Siddharrtha Shankar**  
“A B.Tech student trying to make an evolution in the IT industry.”
