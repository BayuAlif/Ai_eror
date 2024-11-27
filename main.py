import asyncio
import pyttsx3
import speech_recognition as sr
import json
from vtuber_api import VTubeAPI
from open_ai import OpenAIAPI

# Load config
with open("config.json") as f:
    config = json.load(f)

# Initialize APIs
vtube_api = VTubeAPI(config["vtube_ws_url"])
openai_api = OpenAIAPI()

# Text-to-Speech
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Pilih suara (opsional)
    engine.setProperty('rate', 150)  # Atur kecepatan
    engine.setProperty('volume', 1.0)  # Atur volume
    
    # Arahkan output ke VB-Cable jika diperlukan
    engine.setProperty('output_device', 'CABLE Input (VB-Audio Virtual Cable)')
    engine.say(text)
    engine.runAndWait()

# Speech-to-Text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "I couldn't understand that."

# Main function
async def main():
    print("Authenticating with VTube Studio...")
    authenticated = await vtube_api.authenticate("YourPluginName", "YourDeveloperName")
    if not authenticated:
        print("Failed to authenticate with VTube Studio.")
        return

    print("Authentication successful! You can now ask questions.")
    
    # Mendapatkan token autentikasi dari VTube Studio
    token = "YourTokenHere"  # Dapatkan token autentikasi dari API VTube Studio

    # Memuat model dan tokenizer
    tokenizer, model = openai_api.load_model()

    while True:
        question = recognize_speech()
        print(f"You asked: {question}")
        
        # question = "how are you"
        # response = openai_api.ask_question(question, tokenizer, model)
        # print(f"VTuber: {response}")

        
        # if question.lower() == "exit":
        #     break

        # Mendapatkan jawaban dari GPT (T5 dari Hugging Face)
        response = openai_api.ask_question(question, tokenizer, model)
        print(f"VTuber: {response}")
        
        # Mengirim ekspresi ke VTube Studio dan berbicara
        # await vtube_api.send_expression(token, "Smile")  # Ganti dengan ekspresi yang diinginkan
        # speak(response)

# Menjalankan aplikasi utama
asyncio.run(main())
