import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://azureopenai-vastmindz.openai.azure.com/"
openai.api_version = "2022-06-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

generation_prompt = """
You are a friendly AI assistant. You are chatting with a user. Respond to the following message:
User: {}
Your Response:"""

motivational_prompt = """
You are a motivational AI coach, similar to that of Tony Robbins. You are chatting with a user. Try to respond always with uplifting and motiviating messages.
If the user is feeling down or tired, always try to encourage to keep going and push through.
Respond to the following message:
User: {}
Your Response:"""

def generate_response(message):
  
    response = openai.Completion.create(
      engine="Davinci",
      prompt=motivational_prompt.format(message),
      temperature=0,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None
    )

    return response.choices[0].text


if __name__ == "__main__":

    # Generate a response to something
    print(generate_response("How can I structure my day to be more productive?"))