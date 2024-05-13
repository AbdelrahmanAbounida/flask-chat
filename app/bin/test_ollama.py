# https://python.langchain.com/v0.1/docs/integrations/llms/ollama/

# 1- langchain 

# from langchain_community.llms import Ollama

# llm = Ollama(model="gemma:2b")
# query = "Tell me a joke"

# for chunks in llm.stream(query):
#     print(chunks)

# 2- python ollama

import ollama
response = ollama.chat(model='gemma:2b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])

