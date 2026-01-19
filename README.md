# Jarvis – Python Voice Assistant

Jarvis is a simple **voice-controlled personal assistant** built using Python, taking advantage of its simple libraries and easy implementation.  
It can perform tasks like searching Wikipedia, opening websites and applications, playing music, and telling the current time — all using voice commands.

---

## ✨ Features

- 🎙️ Voice recognition using Google Speech API  
- 🗣️ Text-to-speech responses  
- 📚 Wikipedia search and summary  
- 🌐 Open websites like Google & YouTube  
- 🧭 Open installed applications (Firefox, Zen Browser, VS Code, etc.)  
- 🎵 Play music from local directory  
- ⏰ Tell the current time  
- ❌ Voice command to exit the assistant  

---

## 🛠️ Technologies Used

- **Python 3**
- `pyttsx3` – Text to Speech  
- `speech_recognition` – Voice input  
- `wikipedia` – Fetch summaries  
- `datetime` – Time-based greetings  
- `webbrowser` – Open websites  
- `os` – Open local files and applications  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/jarvis-python.git
cd jarvis-python
````

### 2️⃣ Install Required Libraries

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyaudio
```

> ⚠️ **Note:**
> If `pyaudio` fails to install on Windows, install a precompiled wheel from:
> [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

## ▶️ How to Run

```bash
python jarvis.py
```

Make sure your **microphone is connected and working**.

---

## 🖥️ Platform

* Designed for **Windows**
* Uses **SAPI5** for speech output

---

## 🚧 Known Limitations

* Paths to applications are hardcoded (require manual changes)
* Requires active internet for speech recognition & Wikipedia
* No background noise handling yet

---

## 👤 Author

**Upam Deb**
Computer Science Undergraduate
📌 Passionate about AI, automation & system-level programming

