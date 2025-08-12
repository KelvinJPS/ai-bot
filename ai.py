#!/usr/bin/env python3
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

api_key = os.getenv("GENAI_API_KEY")

if not api_key:
    raise ValueError("GENAI_API_KEY environment variable not set.")

client = genai.Client(api_key=api_key)


def ai_reply(message):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""Eres una mastra del horoscopo, tu proposito es ayudar a las personas a conocer su futuro y ayudar en su problemas.
        Empieza el chat con una breve intruduccion, luego ofrece una consulta, y finalmente ofrece ayuda al cliente
        mensaje del cliente:{message}
        """,
    )

    return response.text
