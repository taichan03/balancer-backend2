from dotenv import load_dotenv
import requests
import os
import openai
from flask import Blueprint, request, jsonify

diagnosis_bp = Blueprint('diagnosis', __name__)


@diagnosis_bp.route('/diagnosis', methods=['POST'])
def medication():
    openai.api_key = os.getenv('OPENAI_API_KEY')
    print(os.getenv('OPENAI_API_KEY'))
    data = request.get_json()

    if data is not None:
        diagnosis = data.get('diagnosis')

    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "What are the most commonly prescribed medications for %s?" % diagnosis, }]
    )

    return {'message': ai_response}
