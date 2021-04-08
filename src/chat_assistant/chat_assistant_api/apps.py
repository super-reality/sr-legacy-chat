from django.apps import AppConfig
from django.conf import settings
import os
from transformers import AutoModelForCausalLM, AutoTokenizer


class ProfilesApiConfig(AppConfig):
    name = 'chat_assistant_api'
    
    # Initialize tokenizer and model
    print("Loading GPTDialog model...")
    tokenizer = AutoTokenizer.from_pretrained(settings.MODELS)
    model = AutoModelForCausalLM.from_pretrained(settings.MODELS)
