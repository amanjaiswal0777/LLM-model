# learnd through this repo
Git
Learned git init initializes a Git repository but does not track files.<br>
Used git status to check file states.<br>
Used git ls-files to see tracked files.<br>
Learned the importance of .gitignore for excluding .env, venv/, and __pycache__/.<br>
Understood the basic Git flow: git init → git add → git commit.<br>

LangChain
Learned PromptTemplate for creating dynamic prompts using variables like {topic}.
Learned prompt.invoke() fills the template and returns a PromptValue.
Learned model.invoke() sends the prompt to the chat model and returns an AIMessage.
Learned response.content extracts the generated text.
Used ChatGroq with a Groq API key and openai/gpt-oss-20b.
Understood the difference between model provider and model.
Learned the difference between provider-specific classes (ChatGroq, ChatOpenAI, etc.) and the unified init_chat_model().
Understood that init_chat_model() provides a common way to initialize models across providers; it does not replace PromptTemplate.
