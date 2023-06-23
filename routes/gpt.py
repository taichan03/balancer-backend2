import requests
import os
import openai
import tiktoken
from flask import Blueprint, request, jsonify
from bs4 import BeautifulSoup

gpt_bp = Blueprint('gpt', __name__)

@gpt_bp.route('/wpextraction', methods=['POST'])
def extract_webpage():
    openai.api_key = os.getenv('OPENAI_API_KEY')
    print(os.getenv('OPENAI_API_KEY'))
    data = request.get_json()

    if data is not None:
        webpage_url = data.get('webpage_url')

    response = requests.get(webpage_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_contents = soup.get_text()

    tokens = get_tokens(text_contents, "cl100k_base")

    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Give a brief description of this medicine: %s" % tokens,}]
    )

    return { 'message': ai_response }

def get_tokens(string: str, encoding_name: str) -> str:
    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(string)
    tokens = tokens[:4000]
    output_string = encoding.decode(tokens)
    return output_string