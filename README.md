# learnd through this repo
<h2>Git</h2>

<ul>
  <li>Learned <code>git init</code> initializes a Git repository but does not track files.</li>
  <li>Used <code>git status</code> to check file states.</li>
  <li>Used <code>git ls-files</code> to see tracked files.</li>
  <li>Learned the importance of <code>.gitignore</code> for excluding <code>.env</code>, <code>venv/</code>, and <code>__pycache__/</code>.</li>
  <li>Understood the basic Git flow: <code>git init → git add → git commit</code>.</li>
</ul>

<h2>LangChain</h2>

<ul>
  <li>Learned <code>PromptTemplate</code> for creating dynamic prompts using variables like <code>{topic}</code>.</li>
  <li>Learned <code>prompt.invoke()</code> fills the template and returns a <code>PromptValue</code>.</li>
  <li>Learned <code>model.invoke()</code> sends the prompt to the chat model and returns an <code>AIMessage</code>.</li>
  <li>Learned <code>response.content</code> extracts the generated text.</li>
  <li>Used <code>ChatGroq</code> with a Groq API key and <code>openai/gpt-oss-20b</code>.</li>
  <li>Understood the difference between a model provider and a model.</li>
  <li>Learned the difference between provider-specific classes (<code>ChatGroq</code>, <code>ChatOpenAI</code>, etc.) and the unified <code>init_chat_model()</code>.</li>
  <li>Understood that <code>init_chat_model()</code> provides a common way to initialize models across providers; it does not replace <code>PromptTemplate</code>.</li>
</ul>
