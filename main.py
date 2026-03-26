from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model = "claude-haiku-4-5", temperature = 0.9)
respose = llm.invoke("what is the meaning of life?")
print(respose)


