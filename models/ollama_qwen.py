import os
from dotenv import load_dotenv
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIResponsesModelSettings
from pydantic_ai.providers.ollama import OllamaProvider

load_dotenv()

model_name = os.getenv("OLLAMA_MODEL_QWEN", "qwen3:8b")
ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

# 创建 model
model_ollama_qwen = OpenAIChatModel(
    model_name,
    provider=OllamaProvider(base_url=ollama_base_url),
)

model_ollama_qwen_s = OpenAIChatModel(
    model_name,
    provider=OllamaProvider(base_url=ollama_base_url),
)

settings = OpenAIResponsesModelSettings(
    openai_reasoning_effort="low",
    openai_reasoning_summary="detailed",
)
