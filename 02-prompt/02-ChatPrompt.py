from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt_template = ChatPromptTemplate(
    [
        ("system", "你是个专业并且乐于助人的助手"),
        ("user", "一句话解释并说明什么是{name}"),
    ]
)

model = ChatOpenAI(model="deepseek-chat", temperature=0.7)

prompt = prompt_template.invoke({"name": "LangChain"})

print("======prompt======:", prompt, end="\n\n")

response = model.invoke(prompt)

print("======response======:", response, end="\n\n")
