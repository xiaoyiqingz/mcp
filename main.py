"""
交互式客户端程序
等待用户输入，在输入内容后加上"！"并返回给用户
按 Ctrl-C 可以退出程序
"""

import asyncio
from server import server_run

def main():
    """主函数：处理用户输入并返回带感叹号的内容"""
    print("欢迎使用交互式客户端！")
    print("请输入内容（按 Ctrl-C 退出）：")
    
    try:
       server_run()
            
    except KeyboardInterrupt:
        # 捕获 Ctrl-C 信号
        print("\n\n程序已退出，再见！")
    except EOFError:
        # 捕获 EOF 信号（某些终端环境）
        print("\n\n程序已退出，再见！")

if __name__ == "__main__":
    main()
