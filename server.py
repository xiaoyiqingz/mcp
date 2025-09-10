from anget import create_agent

agent = create_agent()

def server_run():
    while True:
        # 等待用户输入
        user_input = input("> ")
        
        # 在用户输入后加上"！"并返回
        result = agent.run_sync(user_input)
        print(f"返回结果: {result.output}")
        # async with agent.run_stream(user_input) as result:
        #    for message in result.new_messages:
        #        print(message.content, end="", flush=True)

        print()  # 空行分隔