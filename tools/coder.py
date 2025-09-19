from pydantic_ai import Agent
from models.qwen import model_qwen
from prompts.prompt import get_coder_prompt


agent = Agent(
    model=model_qwen,
    system_prompt=get_coder_prompt(),
)


async def modify(prompt: str, file_path: str, begin_line: int = 1) -> str:
    prompt = f"这段代码是从文件{file_path}中低{begin_line}行开始读取的, 请帮我查看一下这段代买是否有错误, 如果有请修改, 并给出修改后的代码: {prompt}"
    result = await agent.run(prompt)
    return result.output


async def generate(prompt: str) -> str:
    result = await agent.run(prompt)
    return result.output
