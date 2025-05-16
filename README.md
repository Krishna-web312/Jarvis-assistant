
🧠 Jarvis: Your Personal AI Assistant
Jarvis is a voice-controlled personal assistant built with Python. It can perform tasks such as opening applications, playing music, retrieving the current time and date, and conducting web searches—all through simple voice commands.

🚀 Features
1) Speech Recognition: Understands voice commands using Google's speech recognition API.

2) Text-to-Speech: Responds to users with synthesized speech via pyttsx3.

3) Application Control: Opens applications like Notepad, Calculator, Chrome, VLC, and more.

4) Media Playback: Plays music from your system's music folder and can stop currently playing music.

5) System Information: Provides the current time and date.

6) Web Interaction: Performs web searches and opens websites like YouTube.

🛠️ Technologies Used
1) speech_recognition: For converting speech to text.

2) pyttsx3: For text-to-speech conversion.

3) psutil: To manage system processes.

4) datetime: For fetching current date and time.

5) webbrowser: For opening web pages.

📦 Installation
1) Install the required dependencies:
pip install -r requirements.txt
Create a requirements.txt file with the following content:
SpeechRecognition
pyttsx3
psutil
2) Ensure you have a working microphone and speakers connected to your system.

🎤 Usage
1) Run the assistant:
python jarvis.py
2) The assistant will greet you and wait for your voice command.
3) Speak your command clearly. For example:
"Open Notepad"
"play music"
"What's the time?"
The assistant will execute the command and provide a voice response.

🧩 Customization
You can customize the assistant's behavior by modifying the perform_task function in jarvis.py. Add or modify the elif blocks to introduce new commands and functionalities.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
