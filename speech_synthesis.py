import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

speech_key, service_region = os.getenv("SPEECH_KEY"), os.getenv("SPEECH_REGION")

def synthesise_speech(text):

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
    speech_config.speech_synthesis_voice_name='en-US-TonyNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

if __name__ == "__main__":

    # Synthesise a response
    synthesise_speech("Hello, how can I help you today, I'm here to be your friendly AI assistant")


