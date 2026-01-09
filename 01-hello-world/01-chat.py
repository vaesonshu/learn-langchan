from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 初始化聊天模型
llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0,
)

# 调用模型
response = llm.invoke("你是谁")

print(response.content)
