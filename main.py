from speech_synthesis import synthesise_speech
from azure_openai import generate_response
import speech_recognition as sr

if __name__ == "__main__":

    # Create a speech recognition object
    r = sr.Recognizer()

    # Energy thresholds are useful for determining when to stop listening
    r.energy_threshold = 200
    r.dynamic_energy_threshold = True

    # Record the user's speech
    with sr.Microphone() as source:
        print("Please speak and 'stop' when you are done.")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    # Print the recorded speech
    print(r.recognize_google(audio))

    # Get the text transcription of the speech
    transcription = r.recognize_google(audio)

    # Generate a response to the message using Azure OpenAI
    response = generate_response(transcription)
    print(response)
    # Generate some speech using the Azure Speech Service
    synthesise_speech(response)