import openai
from dotenv import load_dotenv
load_dotenv()


def write_quote():
    response = openai.chat.completions.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user",
                                                         "content": "Generate today's quote."}])
    return response.choices[0].message.content
