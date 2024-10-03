from typing import Protocol, runtime_checkable
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from llama_cpp import Llama

app = Flask(__name__)
load_dotenv()

@runtime_checkable
class LanguageModel(Protocol):
    def generate_response(self, prompt: str) -> str:
        ...

def create_llama_model() -> LanguageModel:
    model_path = os.getenv('LLAMA_MODEL_PATH')
    model = Llama(model_path=model_path)
    def generate_response(prompt: str) -> str:
        max_tokens = int(os.getenv('MAX_TOKENS', 2000))
        response = model(prompt, max_tokens=max_tokens)
        return response['choices'][0]['text'].strip()
    return generate_response

def create_claude_model() -> LanguageModel:
    def generate_response(prompt: str) -> str:
        pass
    return generate_response

def create_gpt4_model() -> LanguageModel:
    def generate_response(prompt: str) -> str:
        pass
    return generate_response

def get_language_model(model_name: str) -> LanguageModel:
    models = {
        "llama": create_llama_model,
        "claude": create_claude_model,
        "gpt4": create_gpt4_model
    }
    return models.get(model_name, lambda: ValueError(f"Unknown model: {model_name}"))()

default_model_name = os.getenv('DEFAULT_MODEL', 'llama')
default_model = get_language_model(default_model_name)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate_readme():
    readme_text = request.json['readme']
    custom_prompt = request.json['customPrompt']

    prompt = f"""
    Evaluate the GitHub README against the given standards.
    Provide a structured response in the following format (using .md):

    1. Met Criteria:
    - [Criterion 1]
    - [Criterion 2]
    ...

    2. Unmet Criteria:
    - [Criterion 1]: [Brief improvement suggestion]
    - [Criterion 2]: [Brief improvement suggestion]
    ...

    3. Overall Assessment:
    [1-2 sentence summary of the README's quality]

    README:
    {readme_text}

    Standards:
    {custom_prompt}
    """

    try:
        result = default_model(prompt)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)