import os
import subprocess
import speech_recognition as sr

def convert_mp3_to_wav(input_file, output_file):
    command = ["ffmpeg", "-i", input_file, output_file, "-y"]
    result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    if result.returncode != 0:
        print("Error during conversion:", result.stderr.decode())
    else:
        print("Conversion successful")

def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    recognizer = sr.Recognizer()
    wav_path = "temp.wav"
    convert_mp3_to_wav(file_path, wav_path)

    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            return text
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"

file_path = "C:/Users/1/PycharmProjects/AA_classificator/tmp/79723-девочка-уэнсдеи-с-последнеи-парты.mp3"
transcription = transcribe_audio(file_path)
print(transcription)