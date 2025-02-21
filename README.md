# **📸 AI-Powered Image Captioning Tool**  

## **📌 Overview**  
This project generates **AI-powered image captions** using **Convolutional Neural Networks (CNNs) for feature extraction** and **Recurrent Neural Networks (RNNs) for text generation**.  
It is useful for **image accessibility, AI-generated descriptions, and content automation**.

---

## **🚀 Features**  
✔ **AI-generated captions** for images using deep learning  
✔ **Web interface** to upload and analyze images  
✔ **Trained CNN + RNN model** for high accuracy  
✔ **Flask-based API** for easy integration  
✔ **Support for multiple languages (Future Update)**  

---

## **🛠️ Technologies Used**  

| **Technology** | **Purpose** |
|--------------|-------------|
| **Python** | Main programming language |
| **TensorFlow & Keras** | AI model training |
| **OpenCV** | Image processing |
| **Flask** | Web app for uploading images |
| **Numpy & Pandas** | Data handling |

---

## **📂 Project Structure**  

```
/AI_Image_Captioning
│── model.py                   # Train and save the model
│── image_caption.py            # Generate captions for images
│── data_loader.py              # Process dataset
│── app.py                      # Flask web app
│── static/sample.jpg           # Sample image
│── templates/index.html        # Web interface
│── requirements.txt            # Dependencies
│── README.md                   # Documentation
```

---

## **🔧 Installation Guide**  

### **1️⃣ Clone the Repository**  
```sh
gh repo clone prangowda/AI-Powered-Image-Captioning-Tool
cd AI_Image_Captioning
```

### **2️⃣ Install Dependencies**  
```sh
pip install numpy matplotlib tensorflow keras opencv-python pillow flask tqdm nltk
```

### **3️⃣ Run Flask App**  
```sh
python app.py
```
Visit **http://127.0.0.1:5000/** to upload an image.

---

## **📡 API Usage**  
### **Send a POST request to generate a caption for an image**  

#### **🔹 Request Format**  
```http
POST /generate_caption
Content-Type: multipart/form-data
File: image.jpg
```

#### **🔹 Example Response**  
```json
{
  "caption": "A child is playing with a dog in the park."
}
```

---

## **📊 How It Works**  
1. The **CNN model (InceptionV3)** extracts **visual features** from the uploaded image.  
2. These features are **processed by an RNN (LSTM)**, trained on a dataset of captioned images.  
3. The model **generates a text caption** based on the extracted features.  
4. The caption is **displayed on the web interface** or returned via API.

---

## **🎯 Sample Output**  
### **📷 Input Image**  
![Sample Image](static/sample.jpg)  

### **📝 Generated Caption**  
🗨️ **"A man is riding a bike."**  

---

## **🔮 Future Enhancements**  
✅ Add **real-time speech-to-text captions**  
✅ Support **video captioning**  
✅ Deploy as a **Chrome extension**  
✅ Improve **caption accuracy** using transformers  

---

## **🤝 Contributing**  
We welcome contributions! Follow these steps:  
1. **Fork** the repository  
2. **Create** a new branch (`feature-xyz`)  
3. **Commit** your changes  
4. **Push** to your branch and submit a **Pull Request**  
