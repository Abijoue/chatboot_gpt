import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import openai
from pydub import AudioSegment
from pydub.playback import play



# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please start speaking...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Speech recognized: " + text)
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from the Speech Recognition service; {0}".format(e))
    return ""


def chat_with_gpt(text):
    openai.api_key = "################################################""

    chat = []
    chat.append({"role": "system", "content": "You are a moroccan tourist guide ."})
    chat.append({"role": "user", "content": text})
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= chat
    )
    chat_response = res['choices'][0]['message']['content']
    return chat_response

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text, lang='en', tld='com.au')
    tts.save("response.mp3")
    playsound("response.mp3")



# Main program
if __name__ == "__main__":

    # Step 1: Convert speech to text
    spoken_text = speech_to_text()

    # Step 2: Send text to ChatGPT and get response
    gpt_response = chat_with_gpt(spoken_text)

    print('#################################################')
    print(gpt_response)
    print('#################################################')
   
    # Step 3: Convert ChatGPT response to speech
    text_to_speech(gpt_response)
