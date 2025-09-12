import os
from typing import Optional, Any, Type
from dotenv import load_dotenv
from pydantic_ai import Agent, toolsets
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.ollama import OllamaProvider

# 加载 .env 文件中的环境变量
load_dotenv()


def create_agent(
    model_name: Optional[str] = None,
    ollama_base_url: Optional[str] = None,
    system_prompt: Optional[str] = None,
    deps_type: Optional[Type[Any]] = None,
    output_type: Optional[Type[Any]] = None,
    instructions: Optional[str] = None,
    toolsets: Optional[list[toolsets.AbstractToolset]] = None,
) -> Agent:
    """
    创建统一的 Agent 实例

    Args:
        model_name: 模型名称，默认从环境变量 OLLAMA_MODEL 获取
        ollama_base_url: Ollama 基础 URL，默认从环境变量 OLLAMA_BASE_URL 获取
        system_prompt: 系统提示词
        deps_type: 依赖类型
        output_type: 输出类型

    Returns:
        Agent: 配置好的 Agent 实例
    """
    # 从环境变量中获取默认值
    if model_name is None:
        model_name = os.getenv("OLLAMA_MODEL", "deepseek-r1:7b")

    if ollama_base_url is None:
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")

    # 创建模型
    model = OpenAIModel(
        model_name,
        provider=OllamaProvider(base_url=ollama_base_url),
    )

    # 创建 Agent
    agent_kwargs: dict[str, Any] = {"model": model}

    if system_prompt is not None:
        agent_kwargs["system_prompt"] = system_prompt

    if deps_type is not None:
        agent_kwargs["deps_type"] = deps_type

    if output_type is not None:
        agent_kwargs["output_type"] = output_type

    if instructions is not None:
        agent_kwargs["instructions"] = instructions

    if toolsets is not None:
        agent_kwargs["toolsets"] = toolsets

    return Agent(**agent_kwargs)
