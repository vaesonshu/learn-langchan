# PromptTemplate：LangChain 中用于定义“可参数化提示词模板”的核心类
# 属于文本型 Prompt（非多角色）
from langchain_core.prompts import PromptTemplate

# ChatOpenAI：LangChain 对 OpenAI / OpenAI 兼容 Chat 模型的封装
# DeepSeek 提供了 OpenAI 兼容接口，因此可以直接使用
from langchain_openai import ChatOpenAI

# load_dotenv：用于从 .env 文件中加载环境变量（如 API Key、Base URL）
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
# 例如：
# OPENAI_API_KEY=xxx
# OPENAI_BASE_URL=https://api.deepseek.com
load_dotenv()

# 使用 from_template 快速创建一个 PromptTemplate
# 模板中包含一个占位符 {name}
# LangChain 会自动解析出 input_variables=["name"]
prompt_template = PromptTemplate.from_template("一句话解释并说明什么是{name}")

# 打印 PromptTemplate 对象
# 注意：此时 Prompt 还没有被渲染，只是一个“模板定义”
print("======prompt_template======:", prompt_template, end="\n\n")

# 创建 ChatOpenAI 模型实例
# model="deepseek-chat"：指定使用 DeepSeek 的 Chat 模型
# temperature=0.7：回答更有创造性、随机性更高
model = ChatOpenAI(model="deepseek-chat", temperature=0.7)

# 打印模型对象
# 这是一个 Runnable，可通过 invoke() 与模型交互
print("======model======:", model, end="\n\n")

# 调用 PromptTemplate.invoke 渲染模板
# 传入变量 name="LLM"
# invoke 是 LCEL 的统一接口，底层等价于：
# prompt_template.format(name="LLM")
#
# 返回值不是普通字符串，而是 PromptValue 对象
prompt = prompt_template.invoke({"name": "LLM"})

# 打印渲染后的 Prompt
# 实际内容为："一句话解释并说明什么是LLM"
print("======prompt======:", prompt, end="\n\n")

# 调用 Chat 模型
# model.invoke 接收 PromptValue / str / BaseMessage
# LangChain 会自动将 PromptValue 转换为 HumanMessage
# 然后发送给 DeepSeek Chat 模型
#
# 返回值是 AIMessage 对象
response = model.invoke(prompt)

# 打印完整 response 对象
# 包含：
# - content（模型回复文本）
# - additional_kwargs
# - response_metadata
print("======response======:", response, end="\n\n")

# 只打印模型生成的文本内容
# response.content 是最常用的字段
print("======response.content======:", response.content, end="\n\n")
