from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:latest",
    base_url="http://localhost:11434",
)

response = llm.invoke("Say hello in one sentence.")

print(response.content)