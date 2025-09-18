from pydantic_ai import Agent
from models.ollama_qwen import model1
from prompts.prompt import get_coder_prompt


agent = Agent(
    model=model1,
    system_prompt=get_coder_prompt(),
)


async def modify(prompt: str) -> str:
    result = await agent.run(prompt)
    return result.output


async def generate(prompt: str) -> str:
    result = await agent.run(prompt)
    return result.output
