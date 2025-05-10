
# MLOps Project – Rakuten France Multimodal Product Classification

## 📦 Project Deployment – API + Dockerized Solution

### 🧩 Project Context

This project was developed as part of my ML Engineer training at DataScientest.  
The goal was to **deploy a machine learning model as an API** and **containerize it** for reproducibility and production-readiness.

To do this, I reused a previous Data Scientist project:  
👉 **Rakuten France Multimodal Product Classification**, developed during my earlier data science training.

### 🔍 Modeling Recap

The task was to classify e-commerce products using:
- **Textual data** (product title and description)
- **Image data** (product photo)

At the end of the modeling phase, we built a prediction system based on:

- **Text-based classification:**
  - ✅ `Conv1D` and `Simple DNN`

- **Image-based classification:**
  - ✅ `Xception` and `InceptionV3`

- **Bimodal (Text + Image) classification:**
  - ✅ `Conv1D` + `Simple DNN` + `Xception`
  - ✅ `Conv1D` + `Simple DNN` + `InceptionV3`

The bimodal models consistently outperformed the individual ones.

### 🛠️ Deployment Steps

- Load the best models trained on text and image data
- Build a **FastAPI** with endpoints for predictions
- Create a **backend database** with user authentication
- **Containerize** the application using Docker and Docker Compose
- Run tests on authentication, authorization, and prediction endpoints using isolated containers

---

## 🚀 How to Use

```bash
git clone https://github.com/mmecheri/Append_Engineer_Project.git
cd Append_Engineer_Project
./setup.sh
```

The API will be available at:  
[http://localhost:8000](http://localhost:8000)

API documentation available at:  
[http://localhost:8000/docs](http://localhost:8000/docs)

Logs from the tests are saved in:  
`api_tests.log`

---

**Author:** Mourad MECHERI  
**Mentor:** Anthony JAILLET
