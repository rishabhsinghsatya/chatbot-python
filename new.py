import speech_recognition as sr
import pyttsx3
import openai
import gradio as gr

# Set up OpenAI API credentials
openai.api_key = "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"

# Set up SpeechRecognition and pyttsx3
r = sr.Recognizer()
engine = pyttsx3.init()

# Define function to convert speech to text
def get_text():
    with sr.Microphone() as source:
        print("Speak now!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except:
        print("Sorry, I didn't catch that.")
        return None

# Define function to get OpenAI response
def get_response(prompt):
    model_engine = "text-davinci-002"
    prompt = f"{prompt}\n\nResponse:"
    response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )
    return response.choices[0].text.strip()

# Define function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define main function
def main():
    while True:
        # Get user input in speech and convert it to text
        prompt = get_text()
        if prompt is None:
            continue

        # Get OpenAI response and convert it to speech
        response = get_response(prompt)
        speak(response)

if __name__ == "__main__":
    main()



# fuction call on them self
