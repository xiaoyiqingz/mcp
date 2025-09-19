"""
信息处理模块
包含一些常用的 Python 代码示例和工具函数
"""

import datetime
import random
from typing import List, Dict


def get_current_info() -> Dict[str, str]:
    now = datetime.datetime.now()
    return {
        "time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "date": now.strftime("%Y年%m月%d日"),
        "weekday": now.strftime("%A"),
        "timestamp": str(int(now.timestamp())),
    }

def generate_random_numbers(
    count: int = 5, min_val: int = 1, max_val: int = 100
) -> List[int]:
    """生成指定数量的随机数"""
    return [random.randint(min_val, max_val) for _ in range(count)]


def calculate_fibonacci(n: int) -> List[int]:
    """计算斐波那契数列的前n项"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def format_text(text: str, max_length: int = 50) -> str:
    """格式化文本，限制最大长度"""
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."


def create_user_profile(name: str, age: int, email: str) -> Dict[str, str]:
    """创建用户档案"""
    return {
        "name": name,
        "age": str(age),
        "email": email,
        "created_at": datetime.datetime.now().isoformat(),
        "status": "active",
    }


def main():
    """主函数 - 演示各种功能"""
    print("=== 系统信息 ===")
    info = get_current_info()
    for key, value in info.items():
        print(f"{key}: {value}")

    print("\n=== 随机数生成 ===")
    numbers = generate_random_numbers(8, 1, 50)
    print(f"随机数: {numbers}")

    print("\n=== 斐波那契数列 ===")
    fib = calculate_fibonacci(10)
    print(f"前10项: {fib}")

    print("\n=== 文本格式化 ===")
    long_text = "这是一个很长的文本，用来测试文本格式化功能"
    formatted = format_text(long_text, 20)
    print(f"原文本: {long_text}")
    print(f"格式化后: {formatted}")

    print("\n=== 用户档案 ===")
    profile = create_user_profile("张三", 25, "zhangsan@example.com")
    for key, value in profile.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
