<div align="center">
  <img src="assets/banner.png" alt="Jarvis AI Banner" style="width: 100%; max-width: 1000px; border-radius: 12px; margin-bottom: 20px;">

  <h1>🤖 Jarvis AI</h1>
  <p><b>An intelligent, voice-activated personal assistant built with Python.</b></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white" alt="Gemini API">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  </p>
</div>

---

## 📖 Overview

**Jarvis AI** is a Python-based virtual assistant designed to handle general tasks and automate your workflow, similar to Amazon Alexa or Google Assistant. It actively listens for its wake word (`"Jarvis"`), processes natural language voice commands, and responds audibly with synthesized speech. By leveraging the advanced Google Gemini API, NewsAPI, and web automation, Jarvis can seamlessly hold intelligent conversations, fetch top news headlines, play local music library tracks, and navigate the web on your behalf.

<br>

## ✨ Key Features

- **🗣️ Voice Activation:** Continuously listens for the wake word `"Jarvis"` to activate without requiring keyboard input.
- **🧠 Generative AI Responses:** Integrates with Google's powerful **Gemini** models to intelligently answer general knowledge questions and execute complex tasks.
- **📰 Read the News:** Fetches and reads aloud the top daily headlines seamlessly using NewsAPI.
- **🎵 Music Playback:** Instantly plays predefined songs directly from your custom `musicLibrary` into your browser.
- **🌐 Web Navigation:** Automatically opens popular websites like Google, Facebook, YouTube, and LinkedIn based entirely on your voice commands.
- **📢 Local Text-to-Speech:** Uses a dual-mode TTS engine containing `pyttsx3` (offline) and `gTTS` (Google Text-to-Speech) alongside `pygame` for smooth, realistic audio playback.

<br>

## 🚀 Working Demo

<div align="center">
  <!-- Replace assets/demo.png with your actual screen recording or GIF -->
  <img src="assets/demo.png" alt="Jarvis AI Terminal Demo" width="800" style="border-radius: 8px; box-shadow: 0px 4px 15px rgba(0,0,0,0.5);">
  <p><i>Jarvis actively recognizing commands in real-time</i></p>
</div>

<br>

## 🛠️ Tech Stack

### Languages & Frameworks
- **Language:** Python 3.x
- **Audio Playback:** module `pygame`

### Artificial Intelligence & APIs
- **Brain:** [Google Gemini API](https://aistudio.google.com/) 
- **News:** `NewsAPI`

### Speech Engine
- **Voice / Speech Recognition:** `SpeechRecognition`, `pocketsphinx`
- **Text-to-Speech Generation:** `gTTS` (Google TTS), `pyttsx3`

<br>

## ⚙️ Installation & Setup

### 1. Clone the Repository
Clone this repository to your local machine using the following command.
```bash
git clone https://github.com/yourusername/jarvis-AI.git
cd jarvis-AI
```

### 2. Install Dependencies
Ensure you have Python installed. Then, run the following bash command to install all necessary packages globally or within a virtual environment:
```bash
pip install SpeechRecognition pyttsx3 gTTS pygame requests google-generativeai pocketsphinx
```

### 3. Configure API Keys
You need two fundamental API keys for Jarvis to securely source information:
- **Gemini API Key:** Acquire your key from [Google AI Studio](https://aistudio.google.com/).
- **NewsAPI Key:** Acquire your key from [NewsAPI](https://newsapi.org/).

Open `main.py` in your text editor and accurately replace the placeholder strings with your actual keys on the respective configuration lines:
```python
newsapi = "<Your_NewsAPI_Key_Here>"
# ...
import google.generativeai as genai
genai.configure(api_key="<Your_Gemini_API_Key_Here>")
```

<br>

## 🎮 Usage Guide

Once configured, run the main initialization script to launch the AI:
```bash
python main.py
```

1. Your console layout will display: `Initializing Jarvis....`
2. Simply say the wake word **"Jarvis"** out loud.
3. Once Jarvis audibly replies ("Ya") and the console prints `Jarvis Active...`, you can give any voice command:
   - *"Open Google"*
   - *"Play skyfall"* (as defined in your `musicLibrary.py`)
   - *"What is the latest news?"*
   - *"Tell me a joke."*

<br>

## 📁 Project Architecture

```text
jarvis-AI/
├── assets/            # Project graphics and showcase media
├── main.py            # Main application loop handling voice context and queries
├── client.py          # Standalone isolated script for testing Gemini API connections
├── musicLibrary.py    # Dictionary referencing song names to mapped YouTube links
└── README.md          # Primary project documentation
```

<br>

## 🤝 Contributing

Contributions, issues, and innovative feature requests are highly welcome!
Feel free to examine the [issues page](https://github.com/yourusername/jarvis-AI/issues) if you wish to contribute to the code.

## 📝 License

This project is open-source and natively available under the **MIT License**.
