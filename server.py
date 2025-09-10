from anget import create_agent
from datetime import datetime
import logfire
import os

# 配置 logfire 将日志输出到文件而不是控制台
logfire.configure()
logfire.instrument_pydantic_ai()

agent = create_agent()


@agent.tool_plain
def get_current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


async def server_run_stream():
    while True:
        # 等待用户输入
        user_input = input("> ")

        # 在用户输入后加上"！"并返回
        async with agent.run_stream(user_input) as result:
            async for message in result.stream_text(delta=True):
                print(message, end="", flush=True)
            print()  # 换行

        print()  # 空行分隔


def server_run():
    while True:
        user_input = input("> ")

        result = agent.run_sync(user_input)
        print(f"返回结果: {result.output}")
        print()
