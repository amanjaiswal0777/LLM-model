# learnd through this repo
Git<br>
Learned git init initializes a Git repository but does not track files.<br>
Used git status to check file states.<br>
Used git ls-files to see tracked files.<br>
Learned the importance of .gitignore for excluding .env, venv/, and __pycache__/.<br>
Understood the basic Git flow: git init → git add → git commit.<br>
<br>
LangChain<br>
Learned PromptTemplate for creating dynamic prompts using variables like {topic}.<br>
Learned prompt.invoke() fills the template and returns a PromptValue.<br>
Learned model.invoke() sends the prompt to the chat model and returns an AIMessage.<br>
Learned response.content extracts the generated text.<br>
Used ChatGroq with a Groq API key and openai/gpt-oss-20b.<br>
Understood the difference between model provider and model.<br>
Learned the difference between provider-specific classes (ChatGroq, ChatOpenAI, etc.) and the unified init_chat_model().<br>
Understood that init_chat_model() provides a common way to initialize models across providers; it does not replace PromptTemplate.<br>
