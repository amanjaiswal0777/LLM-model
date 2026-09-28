from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")
prompt = PromptTemplate.from_template("Explain {topic} in simple language.")

prompt_value = prompt.invoke({"topic": "RAG"})
response = model.invoke(prompt_value)
print(response.content)
