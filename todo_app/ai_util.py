import os
import requests


class AITodo:
    def __init__(self):
        self.API_URL = 'https://api-inference.huggingface.co/models/google/gemma-2-2b-it'
        self.API_KEY = os.getenv('API_KEY')
        self.headers = {'Authorization': f'Bearer {self.API_KEY}'}

    def generate_llm_response(self, todo_title):
        prompt = f'Think creatively and provide a response to the following TODO: "{todo_title}"'
        try:
            payload = {
                'inputs': prompt,
                'parameters': {'max_new_tokens': 100, 'temperature': 0.7},
            }
            response = requests.post(self.API_URL, headers=self.headers, json=payload)
            generated_text = response.json()[0]['generated_text']
            if generated_text.startswith(prompt):
                generated_text = generated_text[len(prompt):].strip()

            return generated_text

        except Exception as e:
            print(e)
