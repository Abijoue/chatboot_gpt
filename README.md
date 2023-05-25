# chatboot_gpt

chatbot based on ChatGPT, with a unique feature: it will be designed as an interactive Moroccan tourist guide.
The interaction with the chatbot will be done through voice, and it will also respond using a generated voice.

## Usage

### python Applications

In this project, I utilized the Anaconda distribution of Python and Visual Studio Code as my preferred code editor.

<details><summary><b>Show instructions</b></summary>

1. Install the requirements:

    ```sh
   pip install SpeechRecognition
   pip install gTTS
   pip install playsound
   pip install openai
   pip install pydub
    ```

2. get the api key from openIA :
https://www.youtube.com/watch?v=nafDyRsVnXU

2. add the API key to the code  :
    ```diff
    + def chat_with_gpt(text):
    +
    +   openai.api_key = "insert your api key in this area"
    +   
    ```

3. run your code and have fun


### Demonstration Videos

