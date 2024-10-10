import os
from llama_cpp import Llama
from dotenv import load_dotenv
from huggingface_hub import login

class BlueViGptModel:
    def __init__(self):
        load_dotenv()
        self.llm = self.load_model()

    def load_model(self):
        model_name = os.getenv("MODEL_NAME")
        model_cache_dir =  "./model_cache"
        hf_token = os.getenv("HF_TOKEN")

        if hf_token:
            login(hf_token, add_to_git_credential=False)
        else:
            raise ValueError("HF_TOKEN environment variable is not set.")

        llm = Llama.from_pretrained(
            repo_id=model_name,
            filename="unsloth.Q8_0.gguf",
            cache_dir=model_cache_dir
        )
        return llm 

    def get_response(self, user_message):
        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        if response.get('choices'):
            message_content = response['choices'][0]['message']['content']
            return message_content
        else:
            return "Sorry, I couldn't generate a response.", 0, 0

    def get_anonymized_message(self, user_message):
        instruction = (
            "Anonymize the data:\n"
            f"{user_message}\n"
        )

        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": instruction
                }
            ]
        )

        if response.get('choices'):
            message_content = response['choices'][0]['message']['content']
            return message_content
        else:
            return "Sorry, I couldn't generate an anonymized response."

    def grammar_correction(self, user_message):
        instruction = (
            "Grammar correction. Do not provide extra information.\n"
            f"Correct this: '{user_message}'\n"
        )

        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": instruction
                }
            ]
        )

        if response.get('choices'):
            message_content = response['choices'][0]['message']['content']
            return message_content
        else:
            return "Sorry, I couldn't correct the prompt."
