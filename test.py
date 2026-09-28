# from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# load_dotenv()   
# model=ChatOpenAI(model="openai/gpt-oss-20b")
# prompt = PromptTemplate.from_template(
#     "Explain {topic} in simple language."
# )
# prompt_value = prompt.invoke({"topic" : "RAG"})

# result = model.invoke(prompt_value)

# print(result.content)/
import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

# if not os.getenv("GROQ_API_KEY"):
#     raise RuntimeError("GROQ_API_KEY is missing. Add it to your .env file.")

model = ChatGroq(model="openai/gpt-oss-20b")
prompt = PromptTemplate.from_template("Explain {topic} in simple language.")

prompt_value = prompt.invoke({"topic": "RAG"})
response = model.invoke(prompt_value)
print(response.content)
