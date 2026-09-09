🧠 Emotion Detection Application
An AI-powered emotion detection system built with IBM Watson NLP, Python, and Flask.

🌟 Project Overview
Emotion Detection Application is an AI-based web application that analyzes text and identifies the emotions expressed within it.
Powered by the Watson NLP library, the application detects five core emotions and determines which emotion is dominant.
🎭 Emotions Detected
Emotion	Description
😠 Anger	Detects expressions of frustration or anger
🤢 Disgust	Identifies feelings of dislike or disgust
😨 Fear	Detects expressions of worry or fear
😊 Joy	Identifies happiness and positive emotions
😢 Sadness	Detects expressions of sadness


The application also provides confidence scores for each emotion and identifies the dominant emotion.
✨ Features
- 🧠 AI-powered emotion detection
- 🎭 Detects 5 different emotions
- 📊 Provides emotion confidence scores
- 🏆 Identifies the dominant emotion
- 🌐 Interactive Flask web interface
- ⚠️ Handles invalid and blank input
- 🧪 Automated unit testing with Pytest
- 🔍 Static code analysis with Pylint
- 🐍 Built with Python
🛠️ Technologies Used
Python       → Core application
Watson NLP   → Emotion prediction
Flask        → Web application framework
Requests     → API communication
Pytest       → Unit testing
Pylint       → Static code analysis
HTML         → Web interface
JavaScript   → Front-end functionality
📁 Project Structure
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
🚀 How to Run
1️⃣ Navigate to the project
cd final_project
2️⃣ Start the Flask application
python3 server.py
The application will run on:
http://localhost:5000
🧪 Unit Testing
The project includes automated tests for all five supported emotions.
Run the test suite with:
pytest
A successful test run should report:
5 passed
🔍 Static Code Analysis
The Flask server can be analyzed using Pylint:
pylint server.py
The goal is to achieve a 10.00/10 code-quality score.
💡 Example
Input
I think I am having fun
Output
The dominant emotion is joy.
The application also returns confidence scores for:
Anger
Disgust
Fear
Joy
Sadness
🎯 Project Goal
The goal of this project is to demonstrate how AI-powered Natural Language Processing can be integrated into a practical web application to analyze human emotions from text.
👨‍💻 Author
HonestMoth
⭐ Built as an IBM Skills Network final project.
