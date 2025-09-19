from pydantic_ai import Agent
from models.qwen import model_qwen
from prompts.prompt import get_coder_prompt


agent = Agent(
    model=model_qwen,
    system_prompt=get_coder_prompt(),
)


async def modify(prompt: str) -> str:
    prompt = (
        f"请帮我查看一下这段代买是否有错误, 如果有请修改, 并给出修改后的代码: {prompt}"
    )
    result = await agent.run(prompt)
    return result.output


async def generate(prompt: str) -> str:
    result = await agent.run(prompt)
    return result.output
