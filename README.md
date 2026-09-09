# Final Project

## Emotion Detection Application

This project is an AI-based Emotion Detection application developed using the Watson NLP library.
# 🧠 Emotion Detection Application

> **An AI-powered emotion detection system built with IBM Watson NLP, Python, and Flask.**

---

## 🌟 Project Overview

**Emotion Detection Application** is an AI-based web application that analyzes text and identifies the emotions expressed within it.

Powered by the **Watson NLP library**, the application detects five core emotions and determines the dominant emotion.

### 🎭 Emotions Detected

| Emotion | Description |
|:---:|---|
| 😠 **Anger** | Detects expressions of frustration or anger |
| 🤢 **Disgust** | Identifies feelings of dislike or disgust |
| 😨 **Fear** | Detects expressions of worry or fear |
| 😊 **Joy** | Identifies happiness and positive emotions |
| 😢 **Sadness** | Detects expressions of sadness |

---

## ✨ Features

- 🧠 AI-powered emotion detection
- 🎭 Detects **5 different emotions**
- 📊 Provides emotion confidence scores
- 🏆 Identifies the dominant emotion
- 🌐 Interactive Flask web interface
- ⚠️ Handles invalid and blank input
- 🧪 Automated unit testing with Pytest
- 🔍 Static code analysis with Pylint

---

## 🛠️ Technologies Used

- 🐍 **Python**
- 🤖 **IBM Watson NLP**
- 🌐 **Flask**
- 🔗 **Requests**
- 🧪 **Pytest**
- 🔍 **Pylint**
- 🖥️ **HTML**
- ⚡ **JavaScript**

---

## 📁 Project Structure

```text
Emotion-Detector-IBM/
│
├── 📂 final_project/
│   ├── 📂 EmotionDetection/
│   │   ├── __init__.py
│   │   └── emotion_detection.py
│   │
│   ├── server.py
│   └── test_emotion_detection.py
│
├── 📂 static/
│   └── mywebscript.js
│
├── 📂 templates/
│   └── index.html
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 How to Run

### 1. Navigate to the project directory

```bash
cd final_project
```

### 2. Start the Flask application

```bash
python3 server.py
```

The application will run on:

```text
http://localhost:5000
```

---

## 🧪 Unit Testing

The project includes automated unit tests covering all five emotions.

Run the test suite:

```bash
pytest
```

A successful test run should display:

```text
5 passed
```

---

## 🔍 Static Code Analysis

Run Pylint on the Flask server:

```bash
pylint server.py
```

The project aims for a **10.00/10** code-quality score.

---

## 💡 Example

### Input

```text
I think I am having fun
```

### Output

```text
The dominant emotion is joy.
```

The application also provides confidence scores for:

**Anger • Disgust • Fear • Joy • Sadness**

---

## 🎯 Project Goal

The goal of this project is to demonstrate how **AI-powered Natural Language Processing (NLP)** can be integrated into a practical web application to analyze human emotions from text.

---

## 👨‍💻 Author

**HonestMoth**

⭐ *IBM Skills Network Final Project*
