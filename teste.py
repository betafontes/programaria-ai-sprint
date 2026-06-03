import os
from dotenv import load_dotenv

load_dotenv()
print("Ambiente funcionando!")
print("API Key carregada?", os.getenv("ANTHROPIC_API_KEY") is not None)