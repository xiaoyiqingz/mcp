from pydantic_ai import RunContext
from pydantic_ai.messages import ModelMessage
from anget import create_agent
from datetime import datetime
import logfire
from httpx import AsyncClient
from dataclasses import dataclass

# 配置 logfire 将日志输出到文件而不是控制台
logfire.configure()
logfire.instrument_pydantic_ai()


@dataclass
class Deps:
    client: AsyncClient


agent = create_agent(
    deps_type=Deps,
)


@agent.tool_plain
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@agent.tool
async def get_weather(ctx: RunContext[Deps], city: str) -> str:
    url = f"http://wttr.in/{city}?format=3"
    response = await ctx.deps.client.get(url)
    return response.text


async def server_run_stream():
    all_messages: list[ModelMessage] = []
    message_history: list[ModelMessage] | None = None

    async with AsyncClient() as client:
        logfire.instrument_httpx(client, capture_all=True)
        deps = Deps(client=client)

        while True:
            # 等待用户输入
            user_input = input("> ")

            # 在用户输入后加上"！"并返回
            async with agent.run_stream(
                user_input, deps=deps, message_history=all_messages
            ) as result:
                async for message in result.stream_text(delta=True):
                    print(message, end="", flush=True)
                print()  # 换行

            all_messages = all_messages + result.new_messages()
            # 对于stream_text(delta=True)，result.all_messages()和result.new_messages()都不会返回历史信息
            # 所以需要手动将历史信息添加到all_messages中
            # all_messages = result.all_messages()
            # message_history = result.new_messages()
            # print(all_messages)

            print()  # 空行分隔


async def server_run():
    async with AsyncClient() as client:
        logfire.instrument_httpx(client, capture_all=True)
        deps = Deps(client=client)

        while True:
            user_input = input("> ")

            result = agent.run_sync(user_input, deps=deps)
            print(f"返回结果: {result.output}")
            print()
