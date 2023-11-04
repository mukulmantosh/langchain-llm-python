from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm = OpenAI()