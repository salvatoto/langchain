import json
import os

from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.chains import APIChain
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI


def read_open_api_key(file_path):
    with open(file_path, 'r') as file:
        api_key_data = json.load(file)
    return api_key_data['OPENAI_API_KEY']

api_key_file = 'api_keys.json'
open_api_key = read_open_api_key(api_key_file)
os.environ["OPENAI_API_KEY"] = open_api_key

llm = OpenAI(temperature=0)


from langchain.chains.api import open_meteo_docs
chain_new = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)

# Prompt the user for a question
user_question = input("Please enter your question: ")

# Run the chain with the user's question
chain_new.run(user_question)